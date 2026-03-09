-- =============================================================
-- BoardMeeting SQLite-schema
-- Genererat från BoardMeeting.xsd version 3.0
-- Svenska kyrkan e-arkiv
-- =============================================================

PRAGMA foreign_keys = ON;


-- =============================================================
-- MÖTE
-- Rotelementet. Ett XML-dokument motsvarar ett möte.
-- =============================================================

CREATE TABLE IF NOT EXISTS meeting (
    id                  INTEGER PRIMARY KEY,
    meeting_id          TEXT    NOT NULL UNIQUE,    -- meetingHeader/meetingId
    fonds_creator       TEXT    NOT NULL,           -- meetingHeader/fondsCreator (text)
    fonds_creator_id    TEXT    NOT NULL,           -- @creatorId
    fonds_creator_id_type TEXT  NOT NULL,           -- @idType
    governing_body      TEXT    NOT NULL,           -- meetingHeader/governingBody
    meeting_type        TEXT    NOT NULL            -- ordinary | extraordinary | other
        CHECK (meeting_type IN ('ordinary', 'extraordinary', 'other')),
    -- xs:choice: antingen meetingDate/meetingTime eller meetingTimeFrom/meetingTimeTo
    meeting_date        TEXT,                       -- meetingDate (ISO date)
    meeting_time        TEXT,                       -- meetingTime (ISO time)
    meeting_time_from   TEXT,                       -- meetingTimeFrom (ISO datetime)
    meeting_time_to     TEXT,                       -- meetingTimeTo (ISO datetime)
    location            TEXT                        -- meetingHeader/location
);


-- =============================================================
-- KALLELSE
-- =============================================================

CREATE TABLE IF NOT EXISTS notice (
    id          INTEGER PRIMARY KEY,
    meeting_id  INTEGER NOT NULL REFERENCES meeting (id) ON DELETE CASCADE,
    issued_date TEXT    NOT NULL,   -- notice/issuedDate (ISO date)
    issued_by   TEXT,               -- notice/issuedBy/name
    issued_role TEXT,               -- notice/issuedBy/role
    -- noticeDocument
    doc_title   TEXT,               -- notice/noticeDocument/title
    doc_path    TEXT,               -- notice/noticeDocument/file/@path
    doc_format  TEXT                -- notice/noticeDocument/file/@fileFormat
);

CREATE TABLE IF NOT EXISTS notice_recipient (
    id        INTEGER PRIMARY KEY,
    notice_id INTEGER NOT NULL REFERENCES notice (id) ON DELETE CASCADE,
    name      TEXT    NOT NULL,     -- notice/recipients/recipient/name
    role      TEXT    NOT NULL      -- @role: chair | member | deputy | secretary | ...
        CHECK (role IN ('chair', 'member', 'deputy', 'secretary', 'adjunct', 'observer', 'other'))
);

CREATE TABLE IF NOT EXISTS notice_esignature (
    id                        INTEGER PRIMARY KEY,
    notice_id                 INTEGER NOT NULL REFERENCES notice (id) ON DELETE CASCADE,
    signer_name               TEXT,
    signer_role               TEXT
        CHECK (signer_role IN ('chair', 'adjuster', 'secretary', 'other')),
    signature_type            TEXT,
    signature_service_provider TEXT,
    present                   INTEGER NOT NULL CHECK (present IN (0, 1)),  -- xs:boolean
    date_signature_is_verified TEXT,   -- ISO datetime
    esignature_has_existed    INTEGER  CHECK (esignature_has_existed IN (0, 1))
);


-- =============================================================
-- DAGORDNING
-- =============================================================

CREATE TABLE IF NOT EXISTS agenda_item (
    id         INTEGER PRIMARY KEY,
    meeting_id INTEGER NOT NULL REFERENCES meeting (id) ON DELETE CASCADE,
    sort_order INTEGER NOT NULL,        -- @order
    item_number TEXT   NOT NULL,        -- agendaItem/itemNumber
    item_title  TEXT   NOT NULL,        -- agendaItem/itemTitle
    item_type   TEXT                    -- opening | procedural | approval | decision | ...
        CHECK (item_type IN ('opening', 'procedural', 'approval', 'decision',
                             'information', 'report', 'other', 'closing')),
    proposer    TEXT                    -- agendaItem/proposer
);


-- =============================================================
-- ÄRENDEN OCH UNDERÄRENDEN
-- subMatter lagras i samma tabell med parent_matter_id satt.
-- =============================================================

CREATE TABLE IF NOT EXISTS matter (
    id                  INTEGER PRIMARY KEY,
    meeting_id          INTEGER NOT NULL REFERENCES meeting (id) ON DELETE CASCADE,
    parent_matter_id    INTEGER REFERENCES matter (id) ON DELETE CASCADE,  -- NULL = toppärende
    sort_order          INTEGER NOT NULL DEFAULT 0,
    matter_number       TEXT    NOT NULL,   -- matterNumber / subMatterNumber
    agenda_ref_order    INTEGER,            -- agendaRef/@order
    matter_title        TEXT    NOT NULL,   -- matterTitle / subMatterTitle
    matter_description  TEXT,              -- matterDescription
    matter_category     TEXT
        CHECK (matter_category IN ('decision', 'information', 'report', 'other')),
    -- restriction
    restriction_type    TEXT
        CHECK (restriction_type IN ('confidential', 'gdpr', 'integrity', 'other')),
    restriction_legal_basis TEXT,          -- restriction/legalBasis
    restriction_note    TEXT,              -- restriction/restrictionNote
    -- votering (1:1 med matter)
    voting_result       TEXT,              -- voting/votingResult
    voting_method       TEXT
        CHECK (voting_method IN ('open', 'secret')),
    -- beslut
    decision            TEXT               -- decision
);

-- Föredragande och ansvariga (maxOccurs="unbounded" -> separat tabell)
CREATE TABLE IF NOT EXISTS matter_rapporteur (
    id        INTEGER PRIMARY KEY,
    matter_id INTEGER NOT NULL REFERENCES matter (id) ON DELETE CASCADE,
    name      TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS matter_responsible (
    id        INTEGER PRIMARY KEY,
    matter_id INTEGER NOT NULL REFERENCES matter (id) ON DELETE CASCADE,
    name      TEXT    NOT NULL
);


-- =============================================================
-- DIARIEREFERENSER
-- Används av både matter och attachment (via polymorf ref).
-- =============================================================

CREATE TABLE IF NOT EXISTS diary_reference (
    id          INTEGER PRIMARY KEY,
    matter_id   INTEGER REFERENCES matter (id) ON DELETE CASCADE,
    -- (framtida: attachment_id INTEGER REFERENCES attachment (id) ON DELETE CASCADE)
    diary_id    TEXT    NOT NULL,   -- diaryReference/diaryId
    diary_system TEXT,              -- diaryReference/diarySystem
    case_handler TEXT,              -- diaryReference/caseHandler
    diary_title TEXT,               -- diaryReference/diaryTitle
    diary_url   TEXT                -- diaryReference/diaryUrl
);


-- =============================================================
-- YRKANDEN
-- =============================================================

CREATE TABLE IF NOT EXISTS motion (
    id        INTEGER PRIMARY KEY,
    matter_id INTEGER NOT NULL REFERENCES matter (id) ON DELETE CASCADE,
    sort_order INTEGER NOT NULL DEFAULT 0,
    name      TEXT,                 -- motion/name
    motion_text TEXT,               -- motion/motionText
    outcome   TEXT
        CHECK (outcome IN ('approved', 'rejected', 'withdrawn', 'other'))
);


-- =============================================================
-- INDIVIDUELLA RÖSTER (vid öppen votering)
-- =============================================================

CREATE TABLE IF NOT EXISTS individual_vote (
    id        INTEGER PRIMARY KEY,
    matter_id INTEGER NOT NULL REFERENCES matter (id) ON DELETE CASCADE,
    name      TEXT    NOT NULL,     -- individualVote/name
    vote      TEXT    NOT NULL
        CHECK (vote IN ('yes', 'no', 'abstain'))
);


-- =============================================================
-- UTTALANDEN (reservation, särskild mening, särskilt yttrande)
-- =============================================================

CREATE TABLE IF NOT EXISTS statement (
    id             INTEGER PRIMARY KEY,
    matter_id      INTEGER NOT NULL REFERENCES matter (id) ON DELETE CASCADE,
    statement_type TEXT    NOT NULL
        CHECK (statement_type IN ('reservation', 'sarskild-mening',
                                  'sarskilt-yttrande', 'other')),
    name           TEXT,            -- statement/name
    statement_text TEXT             -- statement/statementText
);


-- =============================================================
-- BILAGOR
-- =============================================================

CREATE TABLE IF NOT EXISTS attachment (
    id               INTEGER PRIMARY KEY,
    matter_id        INTEGER NOT NULL REFERENCES matter (id) ON DELETE CASCADE,
    attachment_id    TEXT    NOT NULL,   -- attachmentId (från XML)
    attachment_title TEXT    NOT NULL,   -- attachmentTitle
    attachment_type  TEXT    NOT NULL
        CHECK (attachment_type IN ('appendix', 'supporting-document', 'other')),
    -- restriction
    restriction_type      TEXT
        CHECK (restriction_type IN ('confidential', 'gdpr', 'integrity', 'other')),
    restriction_legal_basis TEXT,
    restriction_note        TEXT,
    -- xs:choice: antingen diaryRef eller file
    diary_id         TEXT,               -- diaryRef/diaryId (om diaryRef används)
    diary_system     TEXT,               -- diaryRef/diarySystem
    file_path        TEXT,               -- file/@path (om file används)
    file_format      TEXT                -- file/@fileFormat
);


-- =============================================================
-- PROTOKOLLHUVUD
-- =============================================================

CREATE TABLE IF NOT EXISTS minutes_header (
    id              INTEGER PRIMARY KEY,
    meeting_id      INTEGER NOT NULL UNIQUE REFERENCES meeting (id) ON DELETE CASCADE,
    minutes_number  TEXT    NOT NULL,   -- minutesHeader/minutesNumber
    meeting_ref     TEXT,               -- minutesHeader/meetingRef
    adjustment_date TEXT,               -- minutesHeader/adjustmentDate (ISO date)
    signing_date    TEXT,               -- minutesHeader/signingDate (ISO date)
    quorum          INTEGER NOT NULL    -- minutes/quorum (xs:boolean)
        CHECK (quorum IN (0, 1)),
    -- posting/anslag
    posted_date     TEXT,               -- posting/postedDate
    removed_date    TEXT,               -- posting/removedDate
    posting_location TEXT,              -- posting/postingLocation
    appeal_deadline  TEXT               -- posting/appealDeadline
);

CREATE TABLE IF NOT EXISTS signatory (
    id               INTEGER PRIMARY KEY,
    minutes_header_id INTEGER NOT NULL REFERENCES minutes_header (id) ON DELETE CASCADE,
    name             TEXT    NOT NULL,
    role             TEXT    NOT NULL
        CHECK (role IN ('chair', 'adjuster', 'secretary', 'other'))
);


-- =============================================================
-- MÖTESDELTAGARE
-- =============================================================

CREATE TABLE IF NOT EXISTS attendee (
    id                INTEGER PRIMARY KEY,
    meeting_id        INTEGER NOT NULL REFERENCES meeting (id) ON DELETE CASCADE,
    role              TEXT    NOT NULL
        CHECK (role IN ('chair', 'member', 'deputy', 'secretary',
                        'adjunct', 'observer', 'other')),
    name              TEXT    NOT NULL,
    group_name        TEXT,               -- attendee/group
    attendance_status TEXT    NOT NULL
        CHECK (attendance_status IN ('present', 'absent', 'excused')),
    substituting_for  TEXT                -- attendee/substitutingFor
);

-- Per-paragraf frånvaro/jäv per deltagare
CREATE TABLE IF NOT EXISTS item_absence (
    id          INTEGER PRIMARY KEY,
    attendee_id INTEGER NOT NULL REFERENCES attendee (id) ON DELETE CASCADE,
    matter_ref  TEXT    NOT NULL,         -- itemAbsence/@matterRef
    reason      TEXT
        CHECK (reason IN ('conflict-of-interest', 'left-meeting',
                          'not-yet-arrived', 'other'))
);


-- =============================================================
-- PROTOKOLLDOKUMENT
-- =============================================================

CREATE TABLE IF NOT EXISTS minutes_document (
    id                INTEGER PRIMARY KEY,
    meeting_id        INTEGER NOT NULL UNIQUE REFERENCES meeting (id) ON DELETE CASCADE,
    title             TEXT    NOT NULL,   -- minutesDocument/title
    original_format   TEXT    NOT NULL
        CHECK (original_format IN ('digital', 'paper')),
    file_path         TEXT    NOT NULL,   -- file/@path
    file_format       TEXT,               -- file/@fileFormat
    -- scanning
    scanned_date      TEXT,
    scanned_by        TEXT,
    resolution        TEXT,
    scanning_system   TEXT
);

CREATE TABLE IF NOT EXISTS esignature (
    id                          INTEGER PRIMARY KEY,
    minutes_document_id         INTEGER NOT NULL
        REFERENCES minutes_document (id) ON DELETE CASCADE,
    signer_name                 TEXT,
    signer_role                 TEXT
        CHECK (signer_role IN ('chair', 'adjuster', 'secretary', 'other')),
    signature_type              TEXT,
    signature_service_provider  TEXT,
    present                     INTEGER NOT NULL CHECK (present IN (0, 1)),
    date_signature_is_verified  TEXT,
    esignature_has_existed      INTEGER CHECK (esignature_has_existed IN (0, 1))
);


-- =============================================================
-- VYER (praktiska hjälpvyer)
-- =============================================================

-- Alla ärenden (toppnivå och underärenden) med mötesinformation
CREATE VIEW IF NOT EXISTS v_all_matters AS
SELECT
    m.meeting_id        AS meeting_pk,
    mh.meeting_id       AS meeting_ref,
    mh.governing_body,
    ma.id               AS matter_pk,
    ma.parent_matter_id,
    ma.matter_number,
    ma.matter_title,
    ma.matter_category,
    ma.decision,
    ma.restriction_type
FROM matter ma
JOIN meeting mh ON mh.id = ma.meeting_id
JOIN meeting m  ON m.id  = ma.meeting_id;

-- Föredragande per ärende
CREATE VIEW IF NOT EXISTS v_matter_rapporteurs AS
SELECT
    ma.matter_number,
    ma.matter_title,
    mh.meeting_id,
    mr.name AS rapporteur
FROM matter_rapporteur mr
JOIN matter  ma ON ma.id = mr.matter_id
JOIN meeting mh ON mh.id = ma.meeting_id;

-- Deltagarlista med jäv
CREATE VIEW IF NOT EXISTS v_attendees_with_absences AS
SELECT
    mh.meeting_id,
    a.name,
    a.role,
    a.attendance_status,
    ia.matter_ref,
    ia.reason
FROM attendee a
JOIN meeting mh ON mh.id = a.meeting_id
LEFT JOIN item_absence ia ON ia.attendee_id = a.id;
