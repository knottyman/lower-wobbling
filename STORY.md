# The Greenhouse at Ballywobble — Story Bible

> This is the canon reference for plot, characters, timeline, tone and open decisions.
> The editable story source is in `story/chapters/` and `story/interludes/`;
> `index.html` is generated output. See `AGENTS.md` for the workflow and
> `CHAPTER_GUIDE.md` for short chapter summaries and navigation.
>
> The online chorus (the r/cork layer) is covered in the section below.

## Logline

An ordinary West Cork village builds a shed, a greenhouse, and a
time-credit ledger, and accidentally invents a way of organising itself
that a bank risk assessor cannot classify and the internet cannot stop
misreading.

## Tone and voice

- Dry, warm, understated. Comic without being jokey.
- Third person, past tense, close on the village as a whole rather than one
  protagonist. Free indirect style; the narrator knows what people are
  thinking but rarely says "he thought."
- Irish-English idiom ("grand", "yer man", "the state of it", "I will in
  my hat"). Spelling is en-GB / Hiberno-English ("realise", "organise").
- Em-dashes and semicolons are used liberally. Sentences are often short
  after long ones for comic timing.
- No exclamation marks in narration. Dialogue may have them.
- The humour is deadpan and comes from understatement, not from jokes.
  A character being wrong is funnier than a character being wacky.

## What the story is *not*

- Not a manifesto. It does not argue that co-ops are better; it shows one
  working and lets the reader decide.
- Not a satire of the village. The village is treated with affection.
- Not a satire of the bank either — Wolseley is earnest, not villainous.
- Not a socialist triumph or a capitalist critique. The book deliberately
  refuses to land on either side. Keep that ambiguity.
- Not preachy about climate, community, or mutual aid. Show, don't tell.
- Not a satire of Cork, Cork people, or Irish online life. The chorus is
  frightened, not stupid.
- Not a textbook. It teaches integral decision-making by showing it, never
  by explaining it. The moment a character lectures the reader on
  sociocracy, the book has failed.

## INTEGRAL framework and the story's direction

The story's original ambition includes making the core systems in Peter
Joseph's INTEGRAL framework understandable through the villagers' everyday
lives. The book should not become a manifesto or a technical manual, but it
must not shrink that ambition into a generic story about people sharing
vegetables and tools. The villagers can draw on existing systems knowledge
and modern technology; they do not have to reinvent everything from scratch.

The five connected systems are:
- **CDS — Collaborative Decision System:** proposals, concerns, degrees of
  support, objections, structured dialogue and recorded decisions.
- **OAD — Open Access Design:** shared designs and instructions that can be
  reused and improved, with attention to materials, repair, lifespan and
  environmental impact.
- **ITC — Integral Time Credits:** contribution records and access values;
  credits are not money and are not intended to become a tradable store of
  power.
- **COS — Cooperative Organization System:** cooperative coordination of
  people, skills, tasks, materials and production.
- **FRS — Feedback & Review System:** monitoring outcomes and sending
  feedback to the parts of the system that can respond.

They form a continuous cycle: a need is identified and a decision made;
design and production are organised; contributions and resource use are
recorded; outcomes are reviewed; and feedback may lead to a revised decision,
design or work arrangement. Nodes can connect and federate through shared
standards and cooperation without a central authority taking over. The
framework is intended to grow voluntarily, beginning alongside the existing
economy.

**The current Shed is an early and partial arrangement, not a fully
implemented INTEGRAL node.** The Board has some family resemblance to the
CDS; Ines's Notebook is a foothold for shared design knowledge; the Ledger
shares some principles with ITC but is not automatically the full ITC model;
the Rota and work groups are early cooperative coordination; and the
villagers' practical reviews are beginnings of feedback and monitoring.
These distinctions matter. Do not silently retrofit the full framework
onto established story mechanisms.

The detailed editorial reference is
[`editorial/INTEGRAL_IN_STORY.md`](editorial/INTEGRAL_IN_STORY.md). It is
based on the author's supplied plain-English guide to the technical paper;
consult it when developing scenes involving the five systems, technology,
resource coordination or federation. `STORY.md` remains the authority for
canon. Any change to established mechanics or unresolved story decisions
requires the author's approval.

## Structure

| # | Section | Kicker | Function |
|---|---------|--------|----------|
| — | prologue | Prologue | Frame: viral misreading. Introduces Wolseley. |
| 1 | the-lettuce | Chapter One | Inciting incident: lettuce, Mabel, Ines, the bucket. |
| 2 | the-money | Chapter Two | Mrs Kavanagh; Odd Jobs co-op; the one-way valve. |
| 3 | not-convinced | Chapter Three | McKenna, O'Driscoll; the supermarket letter. |
| 4 | the-greenhouse | Chapter Four | The gathering, the Board, the Rota, the build. **Both gauge modes demonstrated here.** |
| 5 | the-ledger | Chapter Five | The Ledger explained; Hob declines. |
| 6 | first-winter | Chapter Six | The storm; Gerard's reserve argument. |
| 7 | the-ladders | Chapter Seven | O'Driscoll's fear; the shelves. |
| 8 | supply-chain | Chapter Eight | O'Driscoll becomes a supplier; the valve holds. |
| 9 | the-visitors | Chapter Nine | Scaling questions; Hob signs; Aoife stung. |
| 10 | next-village | Chapter Ten | Drumroe; a different set of problems. |
| 11 | delivery-note | Chapter Eleven | The private delivery note; scaling ≠ copying. |
| — | epilogue | Epilogue | Wolesley's report ("It is a shed."). |
| ◆ | appendix | (none) | Concepts glossary. |

Three interludes sit between sections, outside the `<section>` structure:

| # | Location | Type | Function |
|---|----------|------|----------|
| i1 | between ch1 and ch2 | village noticeboard | Establishes Barry G.; the village's own crank. |
| i2 | between ch4 and ch5 | r/cork thread | First r/cork appearance; the "who owns the greenhouse?" criticism; produces the ownership note. |
| i3 | between ch6 and ch7 | r/cork thread | The "who audits the Ledger?" criticism; produces Donal as second record-keeper. |
| i4 | inside ch9 (after Hob signs) | r/cork thread (screenshot, described) | The Aoife sting; produces shared contact role and the Ledger explainer. |
| i5 | after epilogue | r/cork thread | The thread outlives the story; HealyPass comes round; Barry doesn't. |

Interludes i1–i3 and i5 are marked up as `<div class="noticeboard">` or
`<div class="thread">`. Interlude i4 is described in prose inside ch9
(Aoife brings a printout) rather than rendered as a thread block; the
printout text is the *title* of the thread and the fact that Aoife is
named. Do not convert i4 into a full `.thread` block without the author's
say-so — the point is that Aoife sees it alone, not that the reader reads
it with her.

## Characters

**Mabel Brennan** (71, widow, lifelong Ballywobble). The engine. Dislikes
meetings, "stakeholders", petitions. Difficult to stop once she decides
something is daft. Speaks in short declaratives. Dry. Never sentimental
aloud. She has short, practical grey hair, alert eyes and purposeful
movements; people tend to notice her energy and presence before they
remember her age. Her clothes are comfortable and practical, with a little
individuality rather than a uniform "village grandmother" look. Her humour
is straight-faced and understated: she does not signal a joke or wait for
people to catch it. Her arc: from private grumbler to the person who holds
the structure together without ever claiming to. She insists she hates
meetings and is, by ch4, effectively chairing them; the gap between what
she says and what she does is deliberate and is a running joke. Do not
resolve it by having her admit it.

**Ines Pereira** (20, environmental science student, Portuguese-West Cork, parents
run Stella's café). The systems mind. Fairly attractive in an understated,
natural way, with an observant, knowing expression and a persuasive look
that can make someone feel their arm has been twisted before they quite
notice it happening. That is how she comes across, not a sign that she
knows everything. Her charm is part of her presence, not her whole
personality. She has dark brown, naturally wavy, shoulder-length hair
and brown eyes. Reads forums (the Integral Site), watches and listens widely,
writes things down, designs the Ledger and the Board. She encounters
forceful systems critiques but is selective rather than a disciple: keep
distinct what she consumes, what she believes, and what she puts into
practice. Her defining habit is asking incisive questions that expose
assumptions and practical consequences. She notices the question nobody
has asked yet: who is responsible if the volunteer cannot come; who sees
the delivery list; which parts of a model does another village actually
need? Her questions can be inconvenient and occasionally annoy people,
but they come from curiosity and care, not a desire to show off. When
someone challenges her, her first instinct is to understand why they see
it differently. She listens before deciding; she may still disagree, but
sometimes what she hears changes her mind. She can be stubborn and may
occasionally feel defensive, but she does not treat questions as a route
to her own predetermined answer. She does not have all the answers and
must be willing to have her own assumptions challenged. Her arc: from
enthusiast with a notebook to someone who understands that scaling means
*changing*, not copying. Never becomes a leader; stays a translator. She
is the author's temptation to lecture, and the book must resist it. She
facilitates the Board but never explains it.

**Sam Watts** (42, mechanic, three kids, wife manages accounts). The
reluctant joiner. Good at work, bad at
charging. His arc: from "his wife made him" to the person who says "we
shouldn't promise what we haven't got."

**Hob** (Robert Hobbs; older; fixes things; says little). The conscience.
Refuses the Ledger for two years because he has seen debt poison families.
His arc: declines → watches → signs, quietly, when Gerard talks to him.
He is the story's moral centre and must never become a spokesman. He
signs in ch9, not before. He reads the Ledger every week after signing,
the way he reads manuals.

**Mrs Kavanagh** (retired accountant; red pen; ledger with paper roll).
The rules. "Money comes in at this door." The one-way valve is hers. She
also writes the ownership note after the first r/cork thread. Her arc:
none — she is a fixed point of rigour, and that is the joke.

**Gerard O'Callaghan** (retired agricultural contractor; three sheds;
hoarder). The fear. Arc: from suspicion → reserve argument → gives things
away → talks Hob into signing. "He told everyone it had been his idea."

**Mr O'Driscoll** (hardware shop, 26 years). The threatened incumbent.
Arc: from "you're giving things away" → supplier → advisor on glass
thickness. Never joins. "I'm not a member. I'm just a shop." His arc is
the story's argument that the Shed is not zero-sum. He reads the notes
the Shed pins up, even when he doesn't admit it. He is also the instrument
by which the consent mode of the gauge is taught to the reader (ch4): he
asks the difference between an opinion and an objection, and Ines answers
him plainly.

**Mr Reginald Wolesley** (bank Risk Assessment Officer). The frame.
Earnest, not villainous. His report ends "It is a shed." Comic function:
he is the reader who wants a system and finds one that isn't.

**Aoife** (34, marketing diploma she never used). The amplifier, then the
stung one. Makes the flyer; becomes the only named contact; is named in an
r/cork thread as "the face" of a leaderless thing. Her arc: from visibility
→ sting → sharing the contact role with Piotr and Tunde → "less
interesting is good." She does not quit. She does not break down. She
changes something structural and stays.

**Piotr** (builder, Polish). Quiet competence. Fixes the beds. Becomes a
fixture. Also, after ch9, shares the contact phone with Aoife and Tunde.
Never a plot engine; his presence is the point.

**Tunde** (Nigerian nurse, community hospital). Quiet competence. Fan,
splicing, tea. Shares the contact role with Aoife and Piotr. Same function
as Piotr: the story's answer to the chorus's fear.

**Donal** (Skibbereen, 19–20, sustainable agriculture student). The next
generation and the second record-keeper. Appears in ch4; returns after
ch6 to learn the Ledger from Ines; is referenced in ch9 and the epilogue
as one of the two people who can bring the Ledger to the chapel. His
function is structural, not ornamental — he is the answer to "what
happens when Ines goes to college?"

**Mary O'Shea** (Drumroe, retired community nurse). The next village's
Mabel-equivalent, but different: her problem is delivery, not production.
She appears in ch10–11 and posts as `u/Mary_O_Shea_Drumroe` in the
epilogue thread.

**Andrew** (Drumroe, ex-local-government). Wants a system, a rota, a
responsible person. The comic foil in chs 10–11. He is not wrong; he is
just early.

**Niamh Walsh** (Drumroe grower). "I said a few." Guards against the
volunteer becoming trapped by the thing they volunteered for.

**Barry G.** (noticeboard and r/cork only; never appears in prose). The
online misreader. He is the same man in both places; the r/cork handle
`u/BarryG_NotTheShop` is his attempt at anonymity, and the "NotTheShop"
suffix is a running joke among the Shed members, who know exactly who he
is. He is frightened, not malicious, and must remain pitiable. He does not
have a redemption scene. He quietens. That is all.

## The online chorus (r/cork layer)

The chorus is canon. Six online moments across the book: one village
noticeboard (i1), four r/cork threads (i2, i3, i4, i5), and the general
chatter referenced in the prologue. It exists to dramatise the book's
central tension: a practical, local, non-ideological project being read
through an ideological lens by people who are frightened, and the Shed's
refusal to win the argument on the internet's terms.

**The rule of the chorus.** Every interlude must contain at least one of:

- (a) a fair criticism the Shed cannot immediately answer;
- (b) a sting — a comment that lands personally on a named Shed member;
- (c) a poster who is right about something, even if unpleasantly so.

And at least one of:

- (d) a Shed member's reaction that is not smug;
- (e) a poster the Shed members recognise and like (or pity);
- (f) a correction, deletion, mod note, or derail that shows the thread
  is a real place with its own weather.

If an interlude has only jokes at the posters' expense, cut it.

**Recurring posters.** Keep the cast small. Six recurring handles:

- `u/HealyPass1994` — the anxious asker (Dave Healy, went to school with
  Sam, works in insurance in town). Asks the question everyone is
  thinking. Never cruel. Accepts a fact when corrected. Arc: commune →
  co-op → defends the Shed in the epilogue thread without noticing.
- `u/Ciotog_` — the pedant. Knows the difference between a co-op and a
  commune and cannot let it go. Corrects facts, misses feelings, is
  occasionally wrong. Arc: corrects the same error in every thread,
  increasingly wearily; by the epilogue has stopped replying, and the
  error stands uncorrected. That silence is the point.
- `u/BarryG_NotTheShop` — the village's own crank (same man as the
  noticeboard Barry G.). "I'm only saying what everyone's thinking."
  Capitalises Random Words. Posts at 3am. Frightened of change and
  expressing it badly. Never villainous. Arc: mild suspicion → louder →
  a post that goes too far and is gently corrected → quiet.
- `u/AoifeC_` — the stung one. Posts rarely, carefully, in complete
  sentences, with a professional tone that reads as defensive. Deletes
  comments. Edits them to add "not looking for a fight". Arc: named as
  "the woman in charge" → stung → trains two others to share the contact
  role → posts one calm, unbothered reply that ends the thread → stops
  posting.
- `u/InesEstrella` — the lurker who sometimes speaks. Reads
  everything, posts almost nothing. When she does, it's precise and
  slightly too clever, and she regrets it. She never wins an argument
  online. Arc: reads → drafts → posts once → gets piled on → stops →
  reads again, calmer.
- `u/Mary_O_Shea_Drumroe` — the next village's Mary. Appears late (ch10
  onward). Asks practical questions in the middle of ideological threads.
  Ignores the ideological posts entirely. Arc: asks one practical
  question → returns in the epilogue with "we're doing it differently
  here, it's working grand" → signs off.

**Walk-ons** (use sparingly, never recur): `u/deleted` (a deleted
comment, used once, at the moment a thread is about to turn ugly); a mod
note (`[removed by moderator — keep it civil]`, used twice); a one-off
expert (someone who knows about co-op law or glass or soil, posts once,
is ignored — use once, in ch8).

**What the chorus must never do.** Name a real person, real business, or
real r/cork moderator. Use slurs. Reproduce the anti-Muslim rhetoric the
author has seen online — the chorus's fear is *general* ("these people",
"the newcomers", "you know the type") and is corrected by named villagers
("Tunde is a nurse", "Piotr fixed your lawnmower"). Win: the chorus is
never definitively defeated; it quietens, it moves on, it fixes on something
else. That is the honest ending. Be quoted by a character as if it were a
text: characters *react* to it, they don't analyse it. Appear more than
once per two chapters.

**The structural changes the chorus produces** (these are canon and must
be reflected in the prose, not just the interludes):

1. After i2 ("who owns the greenhouse?"): Mrs Kavanagh writes a
   one-page ownership note, pinned in the chapel. It says the greenhouse
   is held by Odd Jobs, that it can't be sold without a general meeting,
   and that any member can inspect the accounts. It is boring, and that
   is the point. (Referenced in ch5.)
2. After i3 ("who audits the Ledger? what happens when Ines leaves?"):
   Ines begins training Donal as a second record-keeper. (Referenced in
   ch9 and ch10.)
3. After i4 ("Aoife is the face"): Aoife trains Piotr and Tunde to share
   the contact role. She keeps making flyers but stops being the only
   name on them. (Referenced in ch9.)
4. After i4 (the paranoid misreading of the Ledger): the Shed pins a
   plain-language explainer beside the ownership note. Two paragraphs. It
   says what the Ledger is, what it isn't, and that anyone can read it on
   request. (Referenced in the epilogue.)
5. Epilogue: none. The thread outlives the story. The Shed has stopped
   trying to win it.

## Key concepts (must stay consistent)

- **The Shed** — the physical shed, and by extension the whole informal
  institution. Capitalised.
- **The Ledger** — the time-credit book. Credits *fade*. They are *not*
  money. They cannot be exchanged for euros. "Not money. Thanks, with
  arithmetic." One-way valve (Mrs Kavanagh's rule): euros can buy things
  from outside; credits circulate only inside; the two never convert.
- **Odd Jobs** (Ballywobble Odd Jobs) — the registered co-op that invoices
  in euros, pays tax, and buys what the Shed can't make. This is the
  *outside-facing* entity. Don't confuse it with the Ledger.
- **The Board** — the digital board for proposals/objections, with the
  annoyance gauge. It is a joke that is also a real facilitation tool.
  Keep both. See the gauge rule below.
- **The annoyance gauge** — the little readout on the Board tablet. It
  has **two modes** and both are canon:
  - **Conflict mode** (during discussion): reads *ANNOYED / VERY ANNOYED
    / EXTREMELY ANNOYED*. Its function is to trigger a change of format
    (break into smaller groups, report back). It is not a vote and not a
    scoreboard. When it climbs, the facilitator changes *how* people are
    talking, not *what* they are deciding.
  - **Consent mode** (at a decision): reads *AGREED*, or shows a block
    if someone has a principled objection. The facilitator asks "any
    principled objections?"; an opinion is something you'd like changed,
    an objection is something you can't live with; an objection stops the
    proposal and it is amended. Nobody wins; everyone can live with it.
  - Both modes are demonstrated in ch4: conflict mode during the
    argument (the gauge climbs, Mabel breaks the room into groups), and
    consent mode after the groups report back (Ines puts the proposal on
    the Board, O'Driscoll asks the difference between an opinion and an
    objection, the gauge reads AGREED).
  - **Teach it through dialogue, never explanation.** O'Driscoll is the
    instrument: he is confused, he asks the practical question, Ines
    answers it plainly. Do not add a scene where a character explains
    sociocracy to the reader. Do not add a third mode, a numerical scale,
    or a colour code. It is a crude thermometer that works; keep it crude.
- **The Rota** — "the nearest thing Ballywobble had to a manager, and it
  wasn't a person. It was a list." Load-bearing joke. Don't explain it.
- **The Notebook** — Ines's design notebook: materials, energy, labour,
  environmental cost. Distinct from the Ledger. Don't merge them.
- **The Integral Site** — the online forum Ines uses. Never named in
  dialogue as anything grander. It is just a forum.
- **The one-way valve** — the rule that makes the whole thing work.
  Any edit that lets credits buy euros (or vice versa) breaks the story.
- **"It is a shed."** — Wolesley's finding. The story's thesis in
  four words. Do not improve it.

## Timeline

Roughly two years, plus a prologue frame and an epilogue frame.

- Prologue: one Tuesday evening, "two years" before the bank inspection
  (the bank visits ~2 years after the account opened).
- Ch1: spring. Bucket → three lettuces → two eaten by slugs.
- Ch2: shortly after; Mrs Kavanagh formalises Odd Jobs.
- Ch3: McKenna's chiller; O'Driscoll confrontation; supermarket letter.
- Ch4: the gathering; greenhouse planned and built. Donal appears. Both
  gauge modes demonstrated. The first r/cork thread (i2) appears two days
  after the build.
- Ch5: the Ledger explained; Hob declines; O'Leary's gutters; Gerard
  reads the Ledger; Hob still declines. Wolesley sees the ownership
  note on the chapel wall.
- Ch6: greenhouse finished March; first harvest May; storm "the first
  winter" (the book's timeline is loose here — the storm is the first
  *winter after* the build, i.e. ~18 months in). The second r/cork thread
  (i3) appears the morning after the storm. Ines agrees to train Donal as
  second record-keeper.
- Ch7: O'Driscoll, the bolts, the shelves.
- Ch8: O'Driscoll becomes the most reliable supplier. "Best quarter in
  five years." The one-off expert appears in a thread around here
  (referenced only; not a full interlude).
- Ch9: visitors; Andrew's first visit; Hob signs (after Gerard talks to
  him); Aoife is stung by the "she's 34" thread (i4) and shares the
  contact role; the Ledger explainer is pinned up.
- Ch10: Drumroe; Mary; Niamh; the first Saturday.
- Ch11: the private delivery note; scaling ≠ copying.
- Epilogue: Wolesley files the report; the internet moves on; the
  second greenhouse is proposed; the final r/cork thread (i5) shows
  HealyPass defending the Shed, Barry still suspicious, Mary signing off.
  Mabel: "You can only outlast them."

Continuity anchors: the greenhouse is built *after* ch4 and produces by
ch6. Hob signs in ch9, *after* declining in ch5. O'Driscoll supplies in
ch8, *after* confrontation in ch3. Gerard gives things away in ch6, *after*
hoarding in ch1–3, and talks to Hob in ch9. Donal starts training on the
Ledger *after* ch6, not before. Aoife shares the contact role *after* i4,
not before. The ownership note exists from between ch4 and ch5 onward.
The Ledger explainer exists from ch9 onward.

## Recurring motifs (use sparingly; they are seasoning, not structure)

- Lettuce as the unit of ordinary indignation.
- The one-way valve as the story's central mechanism.
- "He told everyone it had been his idea." (Gerard, twice; O'Driscoll,
  once.) A running joke about credit and ego. Don't overuse.
- "That's not a system." / "No. It's the beginning of one." (Wolesley
  and Mabel.) A call-and-response. Use it rarely.
- Tea as load-bearing infrastructure.
- "I'm not joining anything." (Sam, then others.) The story's relationship
  to membership.
- Weather as West Cork realism: damp, mist, salt, turf smoke.
- "You can only outlast them." (Mabel, epilogue.) The book's answer to
  the chorus. Do not repeat it.
- The gauge climbing and falling. Use it as a barometer of the room, not
  as a plot device.

## Style rules for editors

1. **Do not explain the system.** If a character understands it, show them
   using it. Never have a character deliver a lecture on mutual aid or
   sociocracy.
2. **Keep the narrator's distance.** The narrator notices and reports; it
   does not editorialise about capitalism.
3. **Dialogue does the work.** Where possible, convert exposition into
   exchange. Mabel is the best instrument for this; O'Driscoll is the
   best instrument for teaching the decision system.
4. **Comedy from understatement.** No puns in narration. No winking.
5. **New characters must have a function**, not a quirk. The story's cast
   is already large; add people only if they change a decision.
6. **Preserve the en-GB/Hiberno spelling and idiom.** "Grand", "yer man",
   "the state of it", "I will in my hat", "sure look".
7. **The one-way valve is inviolable.** Any plot that lets credits become
   money is off-canon.
8. **Hob does not become a spokesman.** He fixes things and reads the
   Ledger. That is all.
9. **Wolesley is never the villain.** He is the reader.
10. **Endings are understated.** The book ends on a gauge coming down and
    Mabel with a cup of tea. Don't add a triumphant finale.
11. **The chorus is never defeated.** It quietens, it moves on, it fixes on
    something else. Do not write a thread where the Shed wins the
    argument.
12. **The chorus is not a strawman.** Every r/cork thread must contain at
    least one fair criticism or one poster who is right. If an edit
    removes the last fair criticism from a thread, the edit is wrong.
13. **The gauge has two modes, not more.** Conflict during discussion,
    consent at decision. Show both at least once. Teach consent through
    dialogue. Never explain it in narration.
14. **Questions are not speeches.** Ines may expose an assumption with a
    sharp question, but she must not use questions as disguised lectures.
    Let other characters answer, disagree, or be irritated; sometimes the
    question should reveal that Ines herself has missed something.

## Open threads (deliberate; do not resolve without author approval)

- Donal's future beyond second record-keeper. He is a seed, not a plot.
- The second greenhouse (epilogue) is proposed, not built.
- Drumroe's trial is ongoing at the end; no result is given.
- The internet misreading is never corrected; it simply moves on.
- Whether the Shed "scales" is the book's open question. Leave it open.
- The anti-Muslim rhetoric the author has observed online. The chorus
  currently keeps this *general* ("the newcomers", "you know the type")
  and answers it with named villagers ("Tunde is a nurse", "Piotr fixed
  your lawnmower"). Whether the book needs one explicit moment where a
  poster says the quiet part and a villager answers it coldly, briefly,
  with no speech, is an **open authorial decision**. Do not add such a
  moment without explicit approval; if approved, place it in the ch8
  thread and keep it under six lines.
- The second greenhouse's fate. It is proposed in the epilogue and
  blocked at the meeting (O'Driscoll's glass objection). Do not resolve
  whether it gets built. That's the point.

## Appendix (concepts glossary)

The appendix in the text is a table of concepts (Ledger, Rota, Board,
one-way valve, Notebook, Integral Site, etc.). Keep it consistent with
this bible. If you add a concept to the story, add it to the appendix
*and* to this bible.

The appendix should also mention the gauge, if it is expanded: the real
analogue is consent-based decision-making (sociocracy, consent rounds,
temperature checks). Keep the entry short; the appendix is a glossary,
not a manual.
