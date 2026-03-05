## Elementlista 1. Mötesinformation

---

#### SvKGS-SM:1 - *Styrelsemöte*

Rotelementet för ett arkiverat styrelsemöte.

Obligatoriskt.

**XML-element:** `boardMeeting`

---

#### SvKGS-SM:2 - *Mötesinformation*

Samlingselement för grundläggande information om mötet.

Obligatoriskt.

**XML-element:** `meetingHeader`

---

#### SvKGS-SM:3 - *Mötes-id*

Unikt identifikator för mötet.

Obligatoriskt.

**XML-element:** `meetingId`<br/>
**Datatyp:** string

---

#### SvKGS-SM:4 - *Arkivbildare*

Namnet på den enhet vars verksamhet har gett upphov till mötet och vars arkiv protokollet tillhör, t.ex. ett pastorat eller ett stift.

Obligatoriskt.

**XML-element:** `fondsCreator`<br/>
**Datatyp:** string

---

#### SvKGS-SM:5 - *Typ av identifikator*

Anger vilken typ av identifikator som används för arkivbildaren.

Obligatoriskt. Värdet väljs från Värdelista 1.

Möjliga värden: `organisationsnummer`, `aid`.

**XML-element:** `fondsCreator/@idType`<br/>
**Datatyp:** string

---

#### SvKGS-SM:6 - *Arkivbildarens identifikator*

Arkivbildarens organisationsnummer eller arkivbildar-id (aid).

Obligatoriskt.

**XML-element:** `fondsCreator/@creatorId`<br/>
**Datatyp:** string

---

#### SvKGS-SM:7 - *Instans*

Det organ som sammanträder och fattar beslut, t.ex. Kyrkorådet eller Kyrkostyrelsen.

Obligatoriskt.

**XML-element:** `governingBody`<br/>
**Datatyp:** string

---

#### SvKGS-SM:8 - *Mötestyp*

Anger om mötet är ordinarie eller extra.

Obligatoriskt. Värdet väljs från Värdelista 2.

Möjliga värden: `ordinary`, `extraordinary`, `other`.

**XML-element:** `meetingType`<br/>
**Datatyp:** string

---

#### SvKGS-SM:9 - *Mötesdatum*

Datum för mötet.

Obligatoriskt om inte *Mötets starttid* används.

**XML-element:** `meetingDate`<br/>
**Datatyp:** date

---

#### SvKGS-SM:10 - *Mötestid*

Klockslag för mötets början.

**XML-element:** `meetingTime`<br/>
**Datatyp:** time

---

#### SvKGS-SM:11 - *Mötets starttid*

Datum och klockslag för mötets början. Används som alternativ till *Mötesdatum* och *Mötestid*, t.ex. när informationen hämtas från Public 360.

Obligatoriskt om inte *Mötesdatum* används.

**XML-element:** `meetingTimeFrom`<br/>
**Datatyp:** dateTime

---

#### SvKGS-SM:12 - *Mötets sluttid*

Datum och klockslag för mötets slut.

**XML-element:** `meetingTimeTo`<br/>
**Datatyp:** dateTime

---

#### SvKGS-SM:13 - *Plats*

Var mötet hålls.

**XML-element:** `location`<br/>
**Datatyp:** string

---

## Elementlista 2. Kallelse

---

#### SvKGS-SM:14 - *Kallelse*

Samlingselement för information om kallelsen till mötet.

**XML-element:** `notice`

---

#### SvKGS-SM:15 - *Utfärdandedatum*

Datum då kallelsen skickades ut.

Obligatoriskt om elementet *Kallelse* används.

**XML-element:** `notice/issuedDate`<br/>
**Datatyp:** date

---

#### SvKGS-SM:16 - *Utfärdad av*

Samlingselement för uppgifter om den person som utfärdade kallelsen.

**XML-element:** `notice/issuedBy`

---

#### SvKGS-SM:17 - *Namn*

Namn på den person som utfärdade kallelsen.

Obligatoriskt om elementet *Utfärdad av* används.

**XML-element:** `notice/issuedBy/name`<br/>
**Datatyp:** string

---

#### SvKGS-SM:18 - *Roll*

Rollen hos den person som utfärdade kallelsen, t.ex. sekreterare.

**XML-element:** `notice/issuedBy/role`<br/>
**Datatyp:** string

---

#### SvKGS-SM:19 - *Mottagare*

Samlingselement för de som kallades till mötet.

**XML-element:** `notice/recipients`

---

#### SvKGS-SM:20 - *Mottagare*

En enskild person som kallades till mötet.

Elementet kan upprepas.

**XML-element:** `notice/recipients/recipient`

---

#### SvKGS-SM:21 - *Mottagarens roll*

Rollen hos den kallade personen.

Obligatoriskt om elementet *Mottagare* används. Värdet väljs från Värdelista 3.

Möjliga värden: `chair`, `member`, `deputy`, `secretary`, `adjunct`, `observer`, `other`.

**XML-element:** `notice/recipients/recipient/@role`<br/>
**Datatyp:** string

---

#### SvKGS-SM:22 - *Namn*

Namn på den kallade personen.

Obligatoriskt om elementet *Mottagare* används.

**XML-element:** `notice/recipients/recipient/name`<br/>
**Datatyp:** string

---

#### SvKGS-SM:23 - *Kallelsedokument*

Samlingselement för uppgifter om kallelsedokumentet.

**XML-element:** `notice/noticeDocument`

---

#### SvKGS-SM:24 - *Titel*

Kallelsedokumentets titel.

Obligatoriskt om elementet *Kallelsedokument* används.

**XML-element:** `notice/noticeDocument/title`<br/>
**Datatyp:** string

---

#### SvKGS-SM:25 - *Fil*

Referens till kallelsedokumentets fil.

**XML-element:** `notice/noticeDocument/file`

---

#### SvKGS-SM:26 - *Sökväg*

Relativ sökväg till filen i arkivpaketet.

Obligatoriskt om elementet *Fil* används.

**XML-element:** `notice/noticeDocument/file/@path`<br/>
**Datatyp:** string

---

#### SvKGS-SM:27 - *Filformat*

Filens format, t.ex. `PDF/A-2b`.

**XML-element:** `notice/noticeDocument/file/@fileFormat`<br/>
**Datatyp:** string

---

#### SvKGS-SM:28 - *E-signatur*

Uppgifter om eventuell e-signatur på kallelsedokumentet.

Se Elementlista 7. E-signaturer.

**XML-element:** `notice/noticeDocument/eSignature`

---

## Elementlista 3. Dagordning

---

#### SvKGS-SM:29 - *Dagordning*

Samlingselement för mötets planerade punkter.

**XML-element:** `agenda`

---

#### SvKGS-SM:30 - *Dagordningspunkt*

En enskild punkt på dagordningen.

Elementet kan upprepas.

**XML-element:** `agenda/agendaItem`

---

#### SvKGS-SM:31 - *Ordningsnummer*

Dagordningspunktens ordningsnummer.

Obligatoriskt. Måste vara unikt inom dagordningen.

**XML-element:** `agenda/agendaItem/@order`<br/>
**Datatyp:** positiveInteger

---

#### SvKGS-SM:32 - *Paragrafnummer*

Paragrafnummer eller löpnummer för dagordningspunkten, t.ex. `§4`.

Obligatoriskt om elementet *Dagordningspunkt* används.

**XML-element:** `agenda/agendaItem/itemNumber`<br/>
**Datatyp:** string

---

#### SvKGS-SM:33 - *Rubrik*

Dagordningspunktens rubrik.

Obligatoriskt om elementet *Dagordningspunkt* används.

**XML-element:** `agenda/agendaItem/itemTitle`<br/>
**Datatyp:** string

---

#### SvKGS-SM:34 - *Typ av punkt*

Kategorisering av dagordningspunkten.

Värdet väljs från Värdelista 4.

Möjliga värden: `opening`, `procedural`, `approval`, `decision`, `information`, `report`, `other`, `closing`.

**XML-element:** `agenda/agendaItem/itemType`<br/>
**Datatyp:** string

---

#### SvKGS-SM:35 - *Förslagsställare*

Den person eller det organ som lagt fram punkten.

**XML-element:** `agenda/agendaItem/proposer`<br/>
**Datatyp:** string

---

## Elementlista 4. Ärenden

---

#### SvKGS-SM:36 - *Ärenden*

Samlingselement för mötets behandlade ärenden.

**XML-element:** `matters`

---

#### SvKGS-SM:37 - *Ärende*

Ett enskilt ärende som har behandlats på mötet.

Elementet kan upprepas.

**XML-element:** `matters/matter`

---

#### SvKGS-SM:38 - *Paragrafnummer*

Ärendets paragrafnummer i protokollet, t.ex. `§4`.

Obligatoriskt om elementet *Ärende* används.

**XML-element:** `matters/matter/matterNumber`<br/>
**Datatyp:** string

---

#### SvKGS-SM:39 - *Referens till dagordningspunkt*

Kopplar ärendet till rätt dagordningspunkt via dess ordningsnummer.

**XML-element:** `matters/matter/agendaRef`

---

#### SvKGS-SM:40 - *Ordningsnummer*

Ordningsnumret för den dagordningspunkt ärendet hör till.

Obligatoriskt om elementet *Referens till dagordningspunkt* används.

**XML-element:** `matters/matter/agendaRef/@order`<br/>
**Datatyp:** positiveInteger

---

#### SvKGS-SM:41 - *Rubrik*

Ärendets rubrik.

Obligatoriskt om elementet *Ärende* används.

**XML-element:** `matters/matter/matterTitle`<br/>
**Datatyp:** string

---

#### SvKGS-SM:42 - *Ärendekategori*

Kategorisering av ärendet.

Värdet väljs från Värdelista 5.

Möjliga värden: `decision`, `information`, `report`, `other`.

**XML-element:** `matters/matter/matterCategory`<br/>
**Datatyp:** string

---

#### SvKGS-SM:43 - *Sekretess*

Uppgifter om sekretess för ärendet.

Se Elementlista 6. Sekretess.

**XML-element:** `matters/matter/restriction`

---

#### SvKGS-SM:44 - *Föredragande*

Den person som föredrar ärendet på mötet.

Elementet kan upprepas.

**XML-element:** `matters/matter/rapporteur`<br/>
**Datatyp:** string

---

#### SvKGS-SM:45 - *Ansvarig*

Den person som är ansvarig för ärendets beredning.

Elementet kan upprepas.

**XML-element:** `matters/matter/responsible`<br/>
**Datatyp:** string

---

#### SvKGS-SM:46 - *Diariereferenser*

Samlingselement för hänvisningar till ärendets registrering i diariet.

**XML-element:** `matters/matter/diaryReferences`

---

#### SvKGS-SM:47 - *Diariereferens*

Hänvisning till ett diarienummer i ett ärendehanteringssystem.

Elementet kan upprepas.

**XML-element:** `matters/matter/diaryReferences/diaryReference`

---

#### SvKGS-SM:48 - *Diarienummer*

Ärendets diarienummer.

Obligatoriskt om elementet *Diariereferens* används.

**XML-element:** `matters/matter/diaryReferences/diaryReference/diaryId`<br/>
**Datatyp:** string

---

#### SvKGS-SM:49 - *Diariesystem*

Det system där ärendet är registrerat, t.ex. `Public 360`.

**XML-element:** `matters/matter/diaryReferences/diaryReference/diarySystem`<br/>
**Datatyp:** string

---

#### SvKGS-SM:50 - *Dokumenttitel*

Titel på ett specifikt dokument i diariet.

**XML-element:** `matters/matter/diaryReferences/diaryReference/documentTitle`<br/>
**Datatyp:** string

---

#### SvKGS-SM:51 - *Ansvarig handläggare*

Ansvarig handläggare för ärendet i diariesystemet.

**XML-element:** `matters/matter/diaryReferences/diaryReference/caseHandler`<br/>
**Datatyp:** string

---

#### SvKGS-SM:52 - *Beslut*

Beslutets lydelse i klartext.

**XML-element:** `matters/matter/decision`<br/>
**Datatyp:** string

---

#### SvKGS-SM:53 - *Uttalanden*

Samlingselement för reservationer, särskilda meningar och särskilda yttranden kopplade till ärendet.

**XML-element:** `matters/matter/statements`

---

#### SvKGS-SM:54 - *Uttalande*

Ett enskilt uttalande kopplat till ärendet.

Elementet kan upprepas.

**XML-element:** `matters/matter/statements/statement`

---

#### SvKGS-SM:55 - *Typ av uttalande*

Kategorisering av uttalandet.

Obligatoriskt om elementet *Uttalande* används. Värdet väljs från Värdelista 6.

Möjliga värden: `reservation`, `sarskild-mening`, `sarskilt-yttrande`, `other`.

**XML-element:** `matters/matter/statements/statement/@type`<br/>
**Datatyp:** string

---

#### SvKGS-SM:56 - *Namn*

Namn på den ledamot som avger uttalandet.

**XML-element:** `matters/matter/statements/statement/name`<br/>
**Datatyp:** string

---

#### SvKGS-SM:57 - *Text*

Uttalandets lydelse.

**XML-element:** `matters/matter/statements/statement/statementText`<br/>
**Datatyp:** string

---

#### SvKGS-SM:58 - *Bilagor*

Samlingselement för bilagor till ärendet.

Se Elementlista 5. Bilagor.

**XML-element:** `matters/matter/attachments`

---

#### SvKGS-SM:59 - *Underärenden*

Samlingselement för underärenden grupperade under en gemensam paragraf.

**XML-element:** `matters/matter/subMatters`

---

#### SvKGS-SM:60 - *Underärende*

Ett enskilt underärende under en gemensam paragraf.

Elementet kan upprepas.

Underärendet har samma struktur som ett ärende med undantag för referens till dagordningspunkt och underärenden. Se SvKGS-SM:38–58.

**XML-element:** `matters/matter/subMatters/subMatter`

---

## Elementlista 5. Bilagor

---

#### SvKGS-SM:61 - *Bilaga*

Uppgifter om en bilaga kopplad till ett ärende eller underärende.

Elementet kan upprepas.

En bilaga representeras antingen av en diariereferens (om bilagan finns i diariet) eller av en fil (om bilagan inkluderas i arkivleveransen). Dessa är ömsesidigt uteslutande.

**XML-element:** `attachment`

---

#### SvKGS-SM:62 - *Bilage-id*

Unikt id för bilagan.

Obligatoriskt om elementet *Bilaga* används.

**XML-element:** `attachment/attachmentId`<br/>
**Datatyp:** string

---

#### SvKGS-SM:63 - *Titel*

Bilagans rubrik.

Obligatoriskt om elementet *Bilaga* används.

**XML-element:** `attachment/attachmentTitle`<br/>
**Datatyp:** string

---

#### SvKGS-SM:64 - *Typ*

Typ av bilaga.

Obligatoriskt om elementet *Bilaga* används. Värdet väljs från Värdelista 7.

Möjliga värden: `appendix`, `supporting-document`, `other`.

**XML-element:** `attachment/attachmentType`<br/>
**Datatyp:** string

---

#### SvKGS-SM:65 - *Sekretess*

Uppgifter om sekretess för bilagan.

Se Elementlista 6. Sekretess.

**XML-element:** `attachment/restriction`

---

#### SvKGS-SM:66 - *Diariereferens*

Hänvisning till bilagan i diariet. Används om bilagan finns i diariet och inte ska inkluderas i arkivleveransen.

Används inte om elementet *Fil* används.

Se SvKGS-SM:47–51 för underelementens struktur.

**XML-element:** `attachment/diaryRef`

---

#### SvKGS-SM:67 - *Fil*

Referens till bilagans fil i arkivleveransen. Används om bilagan inkluderas i leveransen.

Används inte om elementet *Diariereferens* används.

**XML-element:** `attachment/file`

---

#### SvKGS-SM:68 - *Sökväg*

Relativ sökväg till filen i arkivpaketet.

Obligatoriskt om elementet *Fil* används.

**XML-element:** `attachment/file/@path`<br/>
**Datatyp:** string

---

#### SvKGS-SM:69 - *Filformat*

Filens format, t.ex. `PDF/A-2b`.

**XML-element:** `attachment/file/@fileFormat`<br/>
**Datatyp:** string

---

## Elementlista 6. Sekretess

---

#### SvKGS-SM:70 - *Sekretess*

Samlingselement för uppgifter om sekretess. Kan användas på ärende-, underärende- och bilagenivå.

**XML-element:** `restriction`

---

#### SvKGS-SM:71 - *Typ av sekretess*

Kategorisering av sekretessen.

Obligatoriskt om elementet *Sekretess* används. Värdet väljs från Värdelista 8.

Möjliga värden: `confidential`, `gdpr`, `integrity`, `other`.

**XML-element:** `restriction/restrictionType`<br/>
**Datatyp:** string

---

#### SvKGS-SM:72 - *Lagrum*

Hänvisning till det lagrum som stöder sekretessen, t.ex. `OSL 39 kap. 2 §`.

**XML-element:** `restriction/legalBasis`<br/>
**Datatyp:** string

---

#### SvKGS-SM:73 - *Förklarande text*

Fritext som beskriver sekretessen.

**XML-element:** `restriction/restrictionNote`<br/>
**Datatyp:** string

---

## Elementlista 7. Protokoll

---

#### SvKGS-SM:74 - *Protokoll*

Samlingselement för information om protokollet från mötet.

**XML-element:** `minutes`

---

#### SvKGS-SM:75 - *Protokollhuvud*

Samlingselement för administrativa uppgifter om protokollet.

Obligatoriskt om elementet *Protokoll* används.

**XML-element:** `minutes/minutesHeader`

---

#### SvKGS-SM:76 - *Protokollsnummer*

Protokollets unika identifikator.

Obligatoriskt om elementet *Protokollhuvud* används.

**XML-element:** `minutes/minutesHeader/minutesNumber`<br/>
**Datatyp:** string

---

#### SvKGS-SM:77 - *Mötesreferens*

Referens till mötet via dess *Mötes-id* (SvKGS-SM:3).

**XML-element:** `minutes/minutesHeader/meetingRef`<br/>
**Datatyp:** string

---

#### SvKGS-SM:78 - *Justeringsdatum*

Det datum protokollet justerades. Gäller för beräkning av överklagandefrister.

**XML-element:** `minutes/minutesHeader/adjustmentDate`<br/>
**Datatyp:** date

---

#### SvKGS-SM:79 - *Signeringsdatum*

Det datum det elektroniska protokollet undertecknades.

**XML-element:** `minutes/minutesHeader/signingDate`<br/>
**Datatyp:** date

---

#### SvKGS-SM:80 - *Undertecknare*

Samlingselement för de personer som undertecknar och justerar protokollet.

**XML-element:** `minutes/minutesHeader/signatories`

---

#### SvKGS-SM:81 - *Undertecknare*

En enskild undertecknare av protokollet.

Elementet kan upprepas.

**XML-element:** `minutes/minutesHeader/signatories/signatory`<br/>
**Datatyp:** string

---

#### SvKGS-SM:82 - *Roll*

Undertecknarens roll i förhållande till protokollet.

Obligatoriskt om elementet *Undertecknare* används. Värdet väljs från Värdelista 9.

Möjliga värden: `chair`, `adjuster`, `secretary`, `other`.

**XML-element:** `minutes/minutesHeader/signatories/signatory/@role`<br/>
**Datatyp:** string

---

#### SvKGS-SM:83 - *Anslag*

Samlingselement för uppgifter om protokollets offentliga anslag och överklagandetid.

**XML-element:** `minutes/minutesHeader/posting`

---

#### SvKGS-SM:84 - *Anslagsdatum*

Datum då protokollet anslagits.

**XML-element:** `minutes/minutesHeader/posting/postedDate`<br/>
**Datatyp:** date

---

#### SvKGS-SM:85 - *Datum för nedtagning*

Datum då anslaget togs ned.

**XML-element:** `minutes/minutesHeader/posting/removedDate`<br/>
**Datatyp:** date

---

#### SvKGS-SM:86 - *Plats för anslag*

Var protokollet anslagits, t.ex. `Sunne pastoratkansli, anslagstavla`.

**XML-element:** `minutes/minutesHeader/posting/postingLocation`<br/>
**Datatyp:** string

---

#### SvKGS-SM:87 - *Sista överklagandedag*

Sista dag för överklagande av protokollets beslut.

**XML-element:** `minutes/minutesHeader/posting/appealDeadline`<br/>
**Datatyp:** date

---

#### SvKGS-SM:88 - *Deltagare*

Samlingselement för alla personer som deltog i mötet.

Obligatoriskt om elementet *Protokoll* används.

**XML-element:** `minutes/attendees`

---

#### SvKGS-SM:89 - *Deltagare*

En enskild person som deltog i mötet.

Elementet kan upprepas.

**XML-element:** `minutes/attendees/attendee`

---

#### SvKGS-SM:90 - *Roll*

Deltagarens roll på mötet.

Obligatoriskt om elementet *Deltagare* används. Värdet väljs från Värdelista 3.

Möjliga värden: `chair`, `member`, `deputy`, `secretary`, `adjunct`, `observer`, `other`.

**XML-element:** `minutes/attendees/attendee/@role`<br/>
**Datatyp:** string

---

#### SvKGS-SM:91 - *Namn*

Deltagarens fullständiga namn.

Obligatoriskt om elementet *Deltagare* används.

**XML-element:** `minutes/attendees/attendee/name`<br/>
**Datatyp:** string

---

#### SvKGS-SM:92 - *Nomineringsgrupp*

Den grupp eller det partipolitiskt alternativ som ledamoten representerar.

**XML-element:** `minutes/attendees/attendee/group`<br/>
**Datatyp:** string

---

#### SvKGS-SM:93 - *Närvaro*

Anger om personen var närvarande, frånvarande eller hade anmält förhinder.

Obligatoriskt om elementet *Deltagare* används. Värdet väljs från Värdelista 10.

Möjliga värden: `present`, `absent`, `excused`.

**XML-element:** `minutes/attendees/attendee/attendanceStatus`<br/>
**Datatyp:** string

---

#### SvKGS-SM:94 - *Tjänstgör för*

Anger vem en tjänstgörande ersättare träder in för.

**XML-element:** `minutes/attendees/attendee/substitutingFor`<br/>
**Datatyp:** string

---

#### SvKGS-SM:95 - *Frånvaro per paragraf*

Samlingselement för noteringar om att en deltagare inte var närvarande under en enskild paragraf.

**XML-element:** `minutes/attendees/attendee/itemAbsences`

---

#### SvKGS-SM:96 - *Frånvaro*

En enskild notering om frånvaro under en paragraf.

Elementet kan upprepas.

**XML-element:** `minutes/attendees/attendee/itemAbsences/itemAbsence`

---

#### SvKGS-SM:97 - *Paragrafnummer*

Paragrafnumret för den punkt under vilken personen var frånvarande.

Obligatoriskt om elementet *Frånvaro* används.

**XML-element:** `minutes/attendees/attendee/itemAbsences/itemAbsence/@matterRef`<br/>
**Datatyp:** string

---

#### SvKGS-SM:98 - *Orsak*

Orsaken till frånvaron under den aktuella paragrafen.

Värdet väljs från Värdelista 11.

Möjliga värden: `conflict-of-interest`, `left-meeting`, `not-yet-arrived`, `other`.

**XML-element:** `minutes/attendees/attendee/itemAbsences/itemAbsence/@reason`<br/>
**Datatyp:** string

---

#### SvKGS-SM:99 - *Beslutförhet*

Anger om mötet var beslutfört.

Obligatoriskt om elementet *Protokoll* används.

**XML-element:** `minutes/quorum`<br/>
**Datatyp:** boolean

---

#### SvKGS-SM:100 - *Protokolldokument*

Samlingselement för uppgifter om protokollfilen.

Obligatoriskt om elementet *Protokoll* används.

**XML-element:** `minutes/minutesDocument`

---

#### SvKGS-SM:101 - *Titel*

Protokolldokumentets titel.

Obligatoriskt om elementet *Protokolldokument* används.

**XML-element:** `minutes/minutesDocument/title`<br/>
**Datatyp:** string

---

#### SvKGS-SM:102 - *Originalformat*

Anger om protokollet är ett digitalt original eller ett skannat pappersoriginal.

Obligatoriskt om elementet *Protokolldokument* används. Värdet väljs från Värdelista 12.

Möjliga värden: `digital`, `paper`.

**XML-element:** `minutes/minutesDocument/originalFormat`<br/>
**Datatyp:** string

---

#### SvKGS-SM:103 - *Fil*

Referens till protokollfilen i arkivleveransen.

Obligatoriskt om elementet *Protokolldokument* används.

**XML-element:** `minutes/minutesDocument/file`

---

#### SvKGS-SM:104 - *Sökväg*

Relativ sökväg till protokollfilen i arkivpaketet.

Obligatoriskt om elementet *Fil* används.

**XML-element:** `minutes/minutesDocument/file/@path`<br/>
**Datatyp:** string

---

#### SvKGS-SM:105 - *Filformat*

Protokollfilens format, t.ex. `PDF/A-2b`.

**XML-element:** `minutes/minutesDocument/file/@fileFormat`<br/>
**Datatyp:** string

---

#### SvKGS-SM:106 - *E-signaturer*

Samlingselement för information om elektroniska signaturer på protokollet.

Används när *Originalformat* har värdet `digital`.

**XML-element:** `minutes/minutesDocument/eSignatures`

---

#### SvKGS-SM:107 - *E-signatur*

Information om en enskild elektronisk signatur.

Elementet kan upprepas.

**XML-element:** `minutes/minutesDocument/eSignatures/eSignature`

---

#### SvKGS-SM:108 - *Signatur finns*

Anger om e-signaturen finns.

Obligatoriskt om elementet *E-signatur* används.

**XML-element:** `minutes/minutesDocument/eSignatures/eSignature/@present`<br/>
**Datatyp:** boolean

---

#### SvKGS-SM:109 - *Verifieringsdatum*

Datum och tid då e-signaturen senast verifierades.

**XML-element:** `minutes/minutesDocument/eSignatures/eSignature/@dateSignatureIsVerified`<br/>
**Datatyp:** dateTime

---

#### SvKGS-SM:110 - *Signatur har funnits*

Anger om en e-signatur har funnits men gallrats.

**XML-element:** `minutes/minutesDocument/eSignatures/eSignature/@eSignatureHasExisted`<br/>
**Datatyp:** boolean

---

#### SvKGS-SM:111 - *Undertecknarens namn*

Namn på den person som har signerat.

**XML-element:** `minutes/minutesDocument/eSignatures/eSignature/signerName`<br/>
**Datatyp:** string

---

#### SvKGS-SM:112 - *Undertecknarens roll*

Undertecknarens roll i förhållande till protokollet.

Värdet väljs från Värdelista 9.

Möjliga värden: `chair`, `adjuster`, `secretary`, `other`.

**XML-element:** `minutes/minutesDocument/eSignatures/eSignature/signerRole`<br/>
**Datatyp:** string

---

#### SvKGS-SM:113 - *Signaturstandard*

Den tekniska standard som använts för e-signaturen, t.ex. `PAdES-B-LTA`.

**XML-element:** `minutes/minutesDocument/eSignatures/eSignature/signatureType`<br/>
**Datatyp:** string

---

#### SvKGS-SM:114 - *Signeringstjänst*

Den e-legitimationstjänst som använts för signeringen.

**XML-element:** `minutes/minutesDocument/eSignatures/eSignature/signatureServiceProvider`<br/>
**Datatyp:** string

---

#### SvKGS-SM:115 - *Skanningsuppgifter*

Samlingselement för uppgifter om skanning av pappersoriginal.

Används när *Originalformat* har värdet `paper`.

**XML-element:** `minutes/minutesDocument/scanning`

---

#### SvKGS-SM:116 - *Skanningsdatum*

Datum då skanningen genomfördes.

**XML-element:** `minutes/minutesDocument/scanning/scannedDate`<br/>
**Datatyp:** date

---

#### SvKGS-SM:117 - *Skannat av*

Namn på den person som utförde skanningen.

**XML-element:** `minutes/minutesDocument/scanning/scannedBy`<br/>
**Datatyp:** string

---

#### SvKGS-SM:118 - *Upplösning*

Skanningens upplösning, t.ex. `300dpi`.

**XML-element:** `minutes/minutesDocument/scanning/resolution`<br/>
**Datatyp:** string

---

#### SvKGS-SM:119 - *Skanningsutrustning*

Den utrustning eller det system som användes för skanningen.

**XML-element:** `minutes/minutesDocument/scanning/scanningSystem`<br/>
**Datatyp:** string

---
