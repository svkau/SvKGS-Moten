#!/usr/bin/env python3
"""
boardmeeting_import.py
Importerar ett BoardMeeting XML-dokument till en SQLite-databas.

Användning:
    python boardmeeting_import.py <xml-fil> <databas-fil>

Exempel:
    python boardmeeting_import.py KS_2026_1.xml boardmeeting.db

Scriptet skapar databasen om den inte finns. Om databasen saknar tabeller
körs boardmeeting_create.sql automatiskt (om filen finns i samma katalog).
"""

import sqlite3
import sys
import os
from xml.etree import ElementTree as ET


# ---------------------------------------------------------------------------
# Hjälpfunktioner
# ---------------------------------------------------------------------------

def txt(element, tag):
    """Returnerar texten i ett child-element, eller None om elementet saknas."""
    child = element.find(tag)
    return child.text.strip() if child is not None and child.text else None


def bool_val(s):
    """Konverterar 'true'/'false' till 1/0 för SQLite."""
    if s is None:
        return None
    return 1 if s.strip().lower() == 'true' else 0


def insert(cur, table, data):
    """Infogar en rad i tabellen och returnerar rowid."""
    cols = ', '.join(data.keys())
    placeholders = ', '.join('?' for _ in data)
    cur.execute(f'INSERT INTO {table} ({cols}) VALUES ({placeholders})',
                list(data.values()))
    return cur.lastrowid


# ---------------------------------------------------------------------------
# Import-funktioner per avsnitt
# ---------------------------------------------------------------------------

def import_meeting_header(cur, root):
    header = root.find('meetingHeader')
    fc = header.find('fondsCreator')

    row = {
        'meeting_id':             txt(header, 'meetingId'),
        'fonds_creator':          fc.text.strip() if fc is not None and fc.text else None,
        'fonds_creator_id':       fc.get('creatorId') if fc is not None else None,
        'fonds_creator_id_type':  fc.get('idType') if fc is not None else None,
        'governing_body':         txt(header, 'governingBody'),
        'meeting_type':           txt(header, 'meetingType'),
        'meeting_date':           txt(header, 'meetingDate'),
        'meeting_time':           txt(header, 'meetingTime'),
        'meeting_time_from':      txt(header, 'meetingTimeFrom'),
        'meeting_time_to':        txt(header, 'meetingTimeTo'),
        'location':               txt(header, 'location'),
    }
    return insert(cur, 'meeting', row)


def import_notice(cur, meeting_pk, root):
    notice_el = root.find('notice')
    if notice_el is None:
        return

    issued_by = notice_el.find('issuedBy')
    doc = notice_el.find('noticeDocument')
    doc_file = doc.find('file') if doc is not None else None

    notice_pk = insert(cur, 'notice', {
        'meeting_id':   meeting_pk,
        'issued_date':  txt(notice_el, 'issuedDate'),
        'issued_by':    txt(issued_by, 'name') if issued_by is not None else None,
        'issued_role':  txt(issued_by, 'role') if issued_by is not None else None,
        'doc_title':    txt(doc, 'title') if doc is not None else None,
        'doc_path':     doc_file.get('path') if doc_file is not None else None,
        'doc_format':   doc_file.get('fileFormat') if doc_file is not None else None,
    })

    for rec in notice_el.findall('recipients/recipient'):
        insert(cur, 'notice_recipient', {
            'notice_id': notice_pk,
            'name':      txt(rec, 'name'),
            'role':      rec.get('role'),
        })

    esig = notice_el.find('noticeDocument/eSignature') if doc is not None else None
    if esig is not None:
        insert(cur, 'notice_esignature', {
            'notice_id':                  notice_pk,
            'signer_name':                txt(esig, 'signerName'),
            'signer_role':                txt(esig, 'signerRole'),
            'signature_type':             txt(esig, 'signatureType'),
            'signature_service_provider': txt(esig, 'signatureServiceProvider'),
            'present':                    bool_val(esig.get('present')),
            'date_signature_is_verified': esig.get('dateSignatureIsVerified'),
            'esignature_has_existed':     bool_val(esig.get('eSignatureHasExisted')),
        })


def import_agenda(cur, meeting_pk, root):
    agenda_el = root.find('agenda')
    if agenda_el is None:
        return

    for item in agenda_el.findall('agendaItem'):
        insert(cur, 'agenda_item', {
            'meeting_id':  meeting_pk,
            'sort_order':  int(item.get('order', 0)),
            'item_number': txt(item, 'itemNumber'),
            'item_title':  txt(item, 'itemTitle'),
            'item_type':   txt(item, 'itemType'),
            'proposer':    txt(item, 'proposer'),
        })


def import_restriction(matter_el):
    """Returnerar dict med restriction-fält, eller tomma värden om inget finns."""
    r = matter_el.find('restriction')
    if r is None:
        return {'restriction_type': None,
                'restriction_legal_basis': None,
                'restriction_note': None}
    return {
        'restriction_type':       txt(r, 'restrictionType'),
        'restriction_legal_basis': txt(r, 'legalBasis'),
        'restriction_note':       txt(r, 'restrictionNote'),
    }


def import_diary_references(cur, matter_pk, matter_el):
    for dr in matter_el.findall('diaryReferences/diaryReference'):
        insert(cur, 'diary_reference', {
            'matter_id':    matter_pk,
            'diary_id':     txt(dr, 'diaryId'),
            'diary_system': txt(dr, 'diarySystem'),
            'case_handler': txt(dr, 'caseHandler'),
            'diary_title':  txt(dr, 'diaryTitle'),
            'diary_url':    txt(dr, 'diaryUrl'),
        })


def import_motions(cur, matter_pk, matter_el):
    for motion in matter_el.findall('motions/motion'):
        insert(cur, 'motion', {
            'matter_id':   matter_pk,
            'sort_order':  0,
            'name':        txt(motion, 'name'),
            'motion_text': txt(motion, 'motionText'),
            'outcome':     txt(motion, 'outcome'),
        })


def import_voting(cur, matter_pk, matter_el):
    voting = matter_el.find('voting')
    if voting is None:
        return None, None
    result = txt(voting, 'votingResult')
    method = txt(voting, 'votingMethod')
    for iv in voting.findall('individualVotes/individualVote'):
        insert(cur, 'individual_vote', {
            'matter_id': matter_pk,
            'name':      txt(iv, 'name'),
            'vote':      txt(iv, 'vote'),
        })
    return result, method


def import_statements(cur, matter_pk, matter_el):
    for stmt in matter_el.findall('statements/statement'):
        insert(cur, 'statement', {
            'matter_id':      matter_pk,
            'statement_type': stmt.get('type'),
            'name':           txt(stmt, 'name'),
            'statement_text': txt(stmt, 'statementText'),
        })


def import_attachments(cur, matter_pk, matter_el):
    for att in matter_el.findall('attachments/attachment'):
        r = att.find('restriction')
        file_el = att.find('file')
        diary_el = att.find('diaryRef')
        insert(cur, 'attachment', {
            'matter_id':              matter_pk,
            'attachment_id':          txt(att, 'attachmentId'),
            'attachment_title':       txt(att, 'attachmentTitle'),
            'attachment_type':        txt(att, 'attachmentType'),
            'restriction_type':       txt(r, 'restrictionType') if r is not None else None,
            'restriction_legal_basis': txt(r, 'legalBasis') if r is not None else None,
            'restriction_note':       txt(r, 'restrictionNote') if r is not None else None,
            'diary_id':    txt(diary_el, 'diaryId') if diary_el is not None else None,
            'diary_system': txt(diary_el, 'diarySystem') if diary_el is not None else None,
            'file_path':   file_el.get('path') if file_el is not None else None,
            'file_format': file_el.get('fileFormat') if file_el is not None else None,
        })


def import_matter_element(cur, meeting_pk, matter_el,
                           parent_matter_pk, sort_order,
                           number_tag, title_tag):
    """Importerar ett matter- eller subMatter-element och returnerar dess PK."""
    restr = import_restriction(matter_el)
    voting_result, voting_method = import_voting.__wrapped__ \
        if hasattr(import_voting, '__wrapped__') else (None, None)

    # Votering läses inline här för att kunna lagra i matter-raden
    voting_el = matter_el.find('voting')
    v_result = txt(voting_el, 'votingResult') if voting_el is not None else None
    v_method = txt(voting_el, 'votingMethod') if voting_el is not None else None

    agenda_ref = matter_el.find('agendaRef')

    matter_pk = insert(cur, 'matter', {
        'meeting_id':          meeting_pk,
        'parent_matter_id':    parent_matter_pk,
        'sort_order':          sort_order,
        'matter_number':       txt(matter_el, number_tag),
        'agenda_ref_order':    int(agenda_ref.get('order')) if agenda_ref is not None else None,
        'matter_title':        txt(matter_el, title_tag),
        'matter_description':  txt(matter_el, 'matterDescription'),
        'matter_category':     txt(matter_el, 'matterCategory'),
        **restr,
        'voting_result':       v_result,
        'voting_method':       v_method,
        'decision':            txt(matter_el, 'decision'),
    })

    for name in matter_el.findall('rapporteur'):
        if name.text:
            insert(cur, 'matter_rapporteur',
                   {'matter_id': matter_pk, 'name': name.text.strip()})

    for name in matter_el.findall('responsible'):
        if name.text:
            insert(cur, 'matter_responsible',
                   {'matter_id': matter_pk, 'name': name.text.strip()})

    import_diary_references(cur, matter_pk, matter_el)
    import_motions(cur, matter_pk, matter_el)

    if voting_el is not None:
        for iv in voting_el.findall('individualVotes/individualVote'):
            insert(cur, 'individual_vote', {
                'matter_id': matter_pk,
                'name':      txt(iv, 'name'),
                'vote':      txt(iv, 'vote'),
            })

    import_statements(cur, matter_pk, matter_el)
    import_attachments(cur, matter_pk, matter_el)

    return matter_pk


def import_matters(cur, meeting_pk, root):
    matters_el = root.find('matters')
    if matters_el is None:
        return

    for i, matter_el in enumerate(matters_el.findall('matter')):
        matter_pk = import_matter_element(
            cur, meeting_pk, matter_el,
            parent_matter_pk=None,
            sort_order=i,
            number_tag='matterNumber',
            title_tag='matterTitle',
        )

        sub_matters_el = matter_el.find('subMatters')
        if sub_matters_el is not None:
            for j, sub_el in enumerate(sub_matters_el.findall('subMatter')):
                import_matter_element(
                    cur, meeting_pk, sub_el,
                    parent_matter_pk=matter_pk,
                    sort_order=j,
                    number_tag='subMatterNumber',
                    title_tag='subMatterTitle',
                )


def import_minutes(cur, meeting_pk, root):
    minutes_el = root.find('minutes')
    if minutes_el is None:
        return

    mh = minutes_el.find('minutesHeader')
    posting = mh.find('posting') if mh is not None else None

    minutes_header_pk = insert(cur, 'minutes_header', {
        'meeting_id':      meeting_pk,
        'minutes_number':  txt(mh, 'minutesNumber'),
        'meeting_ref':     txt(mh, 'meetingRef'),
        'adjustment_date': txt(mh, 'adjustmentDate'),
        'signing_date':    txt(mh, 'signingDate'),
        'quorum':          bool_val(txt(minutes_el, 'quorum')),
        'posted_date':     txt(posting, 'postedDate') if posting is not None else None,
        'removed_date':    txt(posting, 'removedDate') if posting is not None else None,
        'posting_location': txt(posting, 'postingLocation') if posting is not None else None,
        'appeal_deadline': txt(posting, 'appealDeadline') if posting is not None else None,
    })

    for sig in (mh.findall('signatories/signatory') if mh is not None else []):
        insert(cur, 'signatory', {
            'minutes_header_id': minutes_header_pk,
            'name':              sig.text.strip() if sig.text else None,
            'role':              sig.get('role'),
        })

    for att in minutes_el.findall('attendees/attendee'):
        name_el = att.find('name')
        name = name_el.text.strip() if name_el is not None and name_el.text else None
        name = name_el.text.strip() if name_el is not None and name_el.text else None

        attendee_pk = insert(cur, 'attendee', {
            'meeting_id':        meeting_pk,
            'role':              att.get('role'),
            'name':              name,
            'group_name':        txt(att, 'group'),
            'attendance_status': txt(att, 'attendanceStatus'),
            'substituting_for':  txt(att, 'substitutingFor'),
        })

        for ia in att.findall('itemAbsences/itemAbsence'):
            insert(cur, 'item_absence', {
                'attendee_id': attendee_pk,
                'matter_ref':  ia.get('matterRef'),
                'reason':      ia.get('reason'),
            })

    doc = minutes_el.find('minutesDocument')
    if doc is not None:
        file_el = doc.find('file')
        scanning = doc.find('scanning')

        doc_pk = insert(cur, 'minutes_document', {
            'meeting_id':      meeting_pk,
            'title':           txt(doc, 'title'),
            'original_format': txt(doc, 'originalFormat'),
            'file_path':       file_el.get('path') if file_el is not None else None,
            'file_format':     file_el.get('fileFormat') if file_el is not None else None,
            'scanned_date':    txt(scanning, 'scannedDate') if scanning is not None else None,
            'scanned_by':      txt(scanning, 'scannedBy') if scanning is not None else None,
            'resolution':      txt(scanning, 'resolution') if scanning is not None else None,
            'scanning_system': txt(scanning, 'scanningSystem') if scanning is not None else None,
        })

        for esig in doc.findall('eSignatures/eSignature'):
            insert(cur, 'esignature', {
                'minutes_document_id':          doc_pk,
                'signer_name':                  txt(esig, 'signerName'),
                'signer_role':                  txt(esig, 'signerRole'),
                'signature_type':               txt(esig, 'signatureType'),
                'signature_service_provider':   txt(esig, 'signatureServiceProvider'),
                'present':                      bool_val(esig.get('present')),
                'date_signature_is_verified':   esig.get('dateSignatureIsVerified'),
                'esignature_has_existed':        bool_val(esig.get('eSignatureHasExisted')),
            })


# ---------------------------------------------------------------------------
# Huvudfunktion
# ---------------------------------------------------------------------------

def import_xml(xml_path, db_path):
    print(f"Läser XML: {xml_path}")
    tree = ET.parse(xml_path)
    root = tree.getroot()

    print(f"Öppnar databas: {db_path}")
    con = sqlite3.connect(db_path)
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()

    # Skapa tabeller om de saknas
    create_script = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'boardmeeting_create.sql')
    if os.path.exists(create_script):
        with open(create_script, encoding='utf-8') as f:
            con.executescript(f.read())
        print("Databastabeller skapade/bekräftade.")
    else:
        print(f"OBS: {create_script} hittades inte – förutsätter att tabellerna redan finns.")

    try:
        meeting_id_text = root.findtext('meetingHeader/meetingId', default='?')
        print(f"Importerar möte: {meeting_id_text}")

        meeting_pk = import_meeting_header(cur, root)
        import_notice(cur, meeting_pk, root)
        import_agenda(cur, meeting_pk, root)
        import_matters(cur, meeting_pk, root)
        import_minutes(cur, meeting_pk, root)

        con.commit()
        print("Import klar.")

        # Summering
        print("\n--- Summering ---")
        for table in ['meeting', 'matter', 'matter_rapporteur', 'diary_reference',
                      'attachment', 'attendee', 'item_absence',
                      'minutes_header', 'signatory', 'minutes_document', 'esignature']:
            count = cur.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            print(f"  {table:<22} {count:>4} rad{'er' if count != 1 else ''}")

    except Exception as e:
        con.rollback()
        print(f"\nFEL – återställer: {e}")
        raise
    finally:
        con.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    import_xml(sys.argv[1], sys.argv[2])
