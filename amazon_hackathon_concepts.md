# Build, Ship, Shape: Amazon Developer Hackathon — Novel Product Concepts

> **Prepared for:** Indian student builder  
> **Submission deadline:** October 23, 2026, 12:00 PM PDT  
> **Research date:** October 17, 2026  
> **Last updated:** October 17, 2026, 11:48 PM IST (Devpost novelty scan complete)  

---

## Capabilities Unlocked in 2025–2026

Understanding what's newly possible is critical — novelty must emerge from **new surfaces**, not just new ideas on old platforms.

### Alexa+ (MCP / Agent Skills) — July 2026 toolkit launch
| Capability | What's new |
|---|---|
| **MCP Server Integration** | Alexa+ acts as an MCP client (Streamable HTTP, spec 2025-11-25). Developers self-host an MCP server; Alexa dynamically discovers and calls your tools via JSON-RPC 2.0. No hardcoded intents needed — the AI agent decides which tool to use. |
| **MCP Apps Extension** | `@modelcontextprotocol/ext-apps` enables rich interactive UI inside Alexa's conversation view — dashboards, maps, multi-step booking flows rendered in webviews. |
| **Natural Discovery** | Your add-on surfaces contextually based on user intent — no "Alexa, open X" invocation required. |
| **OAuth 2.1 + PKCE** | Service-level and user-level auth with account linking. |
| **`alexa-ai` CLI** | Scaffold (`alexa-ai new mcp`), test locally, deploy. Works with cloudflared tunnels. |

> **Source:** [Amazon Alexa+ MCP documentation](https://developer.amazon.com/en-US/docs/alexa/alexa-plus/)

### Bee — Developer access opened mid-2026
| Capability | What's new |
|---|---|
| **Ambient Transcripts** | Bee Frontier (wrist clip) and Bee Eclipse (phone attachment) record, transcribe, and immediately delete raw audio. Output: structured JSON — transcripts, entities, action items, summaries. |
| **Privacy-first architecture** | Customer-controlled encryption keys, no persistent audio storage. Developer integration point is **text-based webhook/API events**, not raw audio streams. |
| **Cross-device connectivity** | Bee transcripts flow into Alexa+, calendars, Gmail/Outlook. Developers build **workflows and agents** on top of structured transcript data. |
| **Hackathon access** | First-ever external developer hackathon track. Bee device or Apple Watch running Bee can connect to real data. |

> **Source:** [bee.computer](https://bee.computer), [aboutamazon.com Bee launch](https://aboutamazon.com)

### Ring — Developer Platform & App Store (2025–2026)
| Capability | What's new |
|---|---|
| **Official REST APIs** | Live WebRTC/RTSP streams, event webhooks (motion, doorbell press, device health), historical clip download (MP4), snapshot pull. Previously developers relied on reverse-engineered unofficial APIs. |
| **Ring App Store** | Third-party apps publishable to millions of Ring users — public and private tracks. |
| **OAuth 2.0 Account Linking** | Granular per-device permission grants. |
| **MCP Server** | Ring provides MCP knowledge bases for AI-assisted development. |

> **Source:** [developer.ring.com](https://developer.ring.com), [Ring API docs via Amazon](https://developer.amazon.com)

### Fire TV / Vega OS — 2026
| Capability | What's new |
|---|---|
| **Vega OS (Linux-based)** | React Native 0.83, React 19 + Compiler, Fabric renderer, Hermes v1 engine. Replaces Android-forked Fire OS on new devices. |
| **`.vpkg` packaging** | Direct Linux packaging instead of APK. Pre-compiled `react-native-reanimated`, `react-native-gesture-handler`, Expo module support. |
| **AI-assisted porting** | Amazon's MCP servers help migrate legacy Fire OS apps to Vega OS via natural language prompts. |
| **Cross-platform monorepo** | Single codebase targeting Vega OS, Fire OS, Apple TV, and Web — ~70% code share. |
| **Content Personalization APIs** | "Continue Watching" rows, Universal Search, Live TV EPG sync, In-App Purchasing. |

> **Source:** [amazondeveloper.com Vega SDK](https://developer.amazon.com/firetv), [Software Mansion Vega partnership](https://swmansion.com)

### AWS Builder & Open Source — Mini-Challenge Tracks
| Capability | What's new |
|---|---|
| **Strands Agents SDK** | Open-source Python/TypeScript framework for building AI agents — agentic loop (Think→Act→Observe), tool definitions, MCP connectivity, local debugging. |
| **Amazon Bedrock AgentCore** | Managed cloud runtime to deploy Strands agents with built-in identity (OAuth/Cognito), memory, gateway, and OpenTelemetry observability — zero infra code. |
| **Amazon Bedrock** | Foundation model API (Claude, etc.) for agent reasoning. |
| **Kiro Crew** | AI coding assistant for collaborative development. |
| **Open Source track** | Create a new public repo OR submit a PR to an existing open-source project during the hackathon. Merged PR not required by deadline. |

> **How it works:** AWS Builder mini-challenge is an **add-on** to your primary track submission. Use AWS services (Bedrock, AgentCore, SageMaker, Strands) in your Ring/Alexa+/Bee/Fire TV project → qualify for the AWS prize pool on top of your track prize.

> **Source:** [Devpost hackathon rules](https://amazonappdev2026.devpost.com), [Strands SDK docs](https://strandsagents.com)

---

## Concept 1: "NyayaSetu" — Voice-First Legal Rights Navigator for Rural India

### The Real-World Problem
**Who suffers:** 70% of India's population lives in areas with fewer than 1 lawyer per 10,000 people. Rural citizens — farmers, daily-wage workers, women facing domestic violence — don't know their basic legal rights under the new Bharatiya Nyaya Sanhita (BNS), land tenancy acts, or NALSA free legal aid schemes. Existing solutions (government portals, Tele-Law helplines) require literacy, smartphone navigation, or waiting days for callbacks.

**Why current solutions fail:**
- Tele-Law (gov.in) requires navigating a web portal or calling during business hours
- Legal chatbots (like Nyaya Mitra) are text-only, require reading ability
- No solution combines voice-first access + structured legal corpus + real-time eligibility checking in one interface

### Amazon Products Used (Technical Mechanism)
**Alexa+ MCP Server (primary) + MCP Apps Extension**

```
Citizen speaks → Alexa+ (MCP client) → Custom MCP Server (FastAPI)
                                          ├── Tool: search_legal_sections(query, state, language)
                                          │     → RAG over BNS/BNSS/Land Acts in ChromaDB
                                          ├── Tool: check_legal_aid_eligibility(income, category)
                                          │     → NALSA rules engine
                                          ├── Tool: find_nearest_dlsa(district)
                                          │     → Geolocation → District Legal Services Authority lookup
                                          └── Resource: recent_judgments(topic)
                                                → Curated precedent summaries

Alexa+ renders results via MCP Apps → interactive card showing:
  - Relevant law section (simplified)
  - Eligibility verdict
  - DLSA office address + phone
  - Disclaimer: "This is informational guidance, not legal representation"
```

**Why Alexa+ is ESSENTIAL:** The target user is illiterate or semi-literate. Voice is the only viable interface. MCP's dynamic tool routing means the system handles open-ended questions ("my landlord is threatening to evict me") without pre-mapped intents — something old Alexa Skills couldn't do.

### Novelty Verification

| Search performed | Result |
|---|---|
| "Alexa skill legal aid India" | No existing Alexa skill for Indian law with MCP architecture. Existing skills are hardcoded FAQ-style (e.g., "Indian Constitution Quiz"). |
| "MCP server legal corpus" | No published MCP server wrapping Indian legal databases found. |
| "voice assistant legal aid rural India" | Tele-Law (gov helpline) and Nyaya Mitra (text chatbot) exist but neither uses voice AI or Alexa. |

**Closest existing thing:** [Tele-Law by DoJ](https://tele-law.in/) — phone-based legal advice through Common Service Centers. Requires human lawyer availability, no AI, no instant answers, text-heavy registration.

### Hackathon Fit
- **Highest scoring criterion:** Potential Impact (access to justice for 800M+ underserved Indians)
- **Quality of Idea:** Novel intersection of MCP agentic architecture + Indian legal corpus
- **Tech Implementation:** MCP server with RAG, OAuth, MCP Apps UI rendering

### 6-Day MVP Build Scope
1. **Day 1–2:** Build MCP server (Python FastAPI + `mcp` SDK) with 3 tools: `search_legal_sections`, `check_legal_aid_eligibility`, `find_nearest_dlsa`. Populate ChromaDB with 50 key BNS sections + 5 state land acts.
2. **Day 3:** Register as Alexa+ add-on via `alexa-ai` CLI. Test with simulated Alexa+ web experience.
3. **Day 4:** Build MCP Apps cards for result rendering (HTML/CSS webview showing law section + eligibility + DLSA info).
4. **Day 5:** Add Hindi language support in tool responses. Record demo conversations.
5. **Day 6:** Record 3-minute demo video showing: farmer asks about land dispute → gets relevant BNS section + DLSA address → check eligibility for free legal aid. Polish README.

---

## Concept 2: "GaliGuard" — Ring-Powered Stray Cattle & Street Hazard Alert Network for Indian Neighborhoods

### The Real-World Problem
**Who suffers:** Residents of Tier-2/3 Indian towns where stray cattle, bulls, and sometimes monkeys roam freely on residential streets. Over 11,000 road accidents per year in India involve stray cattle ([NCRB data](https://ncrb.gov.in)). Two-wheeler riders at night are particularly vulnerable. Stray cattle also damage parked vehicles and block narrow gali (lanes).

**Why current solutions fail:**
- Ring's native "Animal Detected" alert is generic — doesn't distinguish a cow from a cat
- No automated system alerts the neighborhood WhatsApp group
- Municipal cattle-catchers respond to complaints after days, not in real-time
- Ring's "Neighbors" community app has near-zero adoption in India

### Amazon Products Used (Technical Mechanism)
**Ring API (primary) + Alexa+ MCP Server (secondary)**

```
Ring Camera (street-facing) → Motion webhook fires
  → Your backend receives event + pulls snapshot via Ring API
  → Snapshot → YOLOv8 custom model (trained on Indian street animals:
      cow, bull, buffalo, monkey, dog-pack)
  → If cattle/monkey detected:
      ├── Push alert to neighborhood Telegram/WhatsApp bot
      │     "🐄 Stray bull detected outside House #14, Shastri Nagar, 11:42 PM"
      │     + snapshot image + Ring clip link
      ├── Log to MCP Server tool: log_hazard(location, animal_type, timestamp)
      └── Alexa+ MCP Resource: get_hazard_history(neighborhood)
            → "3 cattle incidents this week on Road 4"

Alexa+ integration allows:
  "Alexa, is the lane clear?" → MCP server checks last 30 min of detections
  "Alexa, show cattle incidents this week" → MCP Apps renders heatmap
```

**Why Ring is ESSENTIAL:** Ring's official webhook-driven event API + WebRTC snapshot access is the data source. Without it, you'd need to buy and configure a custom IP camera + build your own motion detection pipeline. Ring provides the hardware, the event trigger, and the clip storage.

### Novelty Verification

| Search performed | Result |
|---|---|
| "Ring camera stray cattle detection India" | No existing Ring App Store app for Indian stray animal classification. Ring's "Search Party" is for lost pet dogs only. |
| "smart camera cow bull detection street alert" | Custom Frigate NVR + YOLO setups exist for home-hosted CCTV, but nothing integrated with Ring's official API or community-alert workflow. |
| "stray cattle road alert system India" | Handful of research papers on CCTV-based cattle detection on highways (NHAI), but no consumer product or Ring integration. |

**Closest existing thing:** [Frigate NVR](https://frigate.video/) — open-source self-hosted NVR with custom object detection. But it requires your own camera, your own NVR server, and doesn't integrate with Ring's ecosystem or Alexa+.

### Hackathon Fit
- **Highest scoring criterion:** Quality of Idea (solves a uniquely Indian problem using Ring's newly opened API in a way Ring's own team hasn't imagined)
- **Potential Impact:** Directly prevents road accidents and property damage
- **Design:** Cross-device UX — Ring notification → Telegram alert → Alexa voice query

### 6-Day MVP Build Scope
1. **Day 1–2:** Set up Ring Developer account, configure OAuth flow, build webhook receiver (Node.js) that captures motion events + pulls snapshots.
2. **Day 3:** Fine-tune YOLOv8-nano on ~500 images of Indian street cattle/monkeys/dogs (use Roboflow for quick labeling). Deploy as serverless inference endpoint.
3. **Day 4:** Build Telegram bot that receives classified alerts with image. Build MCP server with `log_hazard` and `get_hazard_history` tools.
4. **Day 5:** Register Alexa+ add-on for voice queries ("is the lane clear?"). Build MCP Apps card for weekly heatmap.
5. **Day 6:** Record demo video — show Ring detecting cattle at night → Telegram alert fires → Alexa reports "2 incidents tonight on your street." Polish code + README.

---

## Concept 3: "VaniVault" — Bee-Powered Oral History Preservation Engine for Dying Indian Languages

### The Real-World Problem
**Who suffers:** India has 197 endangered languages (UNESCO Atlas). Elders who are the last speakers of tribal and micro-regional dialects are dying without their stories, songs, and vocabularies being recorded. Linguistic researchers have no scalable, ambient capture tool — they use bulky recorders, intimidate speakers, and create artificial interview settings that suppress natural speech.

**Why current solutions fail:**
- Traditional fieldwork recording is expensive, requires trained linguists, and captures only formal interviews
- Otter.ai / Google Recorder transcribe only major languages
- No tool captures natural, ambient elder conversations and auto-structures them into a preservable linguistic corpus
- Raw audio is too unstructured to be useful without entity extraction, speaker diarization, and topic tagging

### Amazon Products Used (Technical Mechanism)
**Bee (primary) + Alexa+ MCP Server + Fire TV**

```
Linguist or family member wears Bee Frontier during natural conversation with elder
  → Bee captures ambient dialogue, processes to transcript + summaries
  → Bee webhook/API pushes structured JSON to your backend:
      {
        "transcript": "...", 
        "speakers": ["elder_speaker", "grandchild"],
        "entities": ["village_name", "folk_character"],
        "language_detected": "Gondi"  // or "unknown/unclassified"
      }

Your backend (MCP Server):
  ├── Tool: tag_linguistic_artifacts(transcript)
  │     → NLP pipeline extracts: unique vocabulary, proverbs, song fragments,
  │       kinship terms, place names, narrative structures
  ├── Tool: build_word_list(language, session_ids)
  │     → Aggregates across sessions → growing lexicon
  ├── Resource: get_language_corpus(language)
  │     → Returns structured corpus for researchers
  └── Tool: generate_story_card(session_id)
        → Creates visual story card with key quotes, translated summaries

Fire TV App (Vega OS / React Native):
  → Family browses recorded stories on the living room TV
  → "Dadi ki Kahaniyaan" — each session rendered as an episode card
  → Plays back transcript with AI-generated illustrations
  → Subtitles in Hindi/English alongside original dialect
```

**Why Bee is ESSENTIAL:** Bee's ambient, non-intrusive form factor is the breakthrough. An elder speaking naturally while wearing a small clip produces far richer linguistic data than a formal interview with a microphone pointed at them. Bee's automatic transcript + entity extraction pipeline eliminates hours of manual transcription.

### Novelty Verification

| Search performed | Result |
|---|---|
| "Bee wearable language preservation endangered" | No results. Bee has never been positioned for linguistic fieldwork. |
| "ambient recording endangered language documentation" | Academic papers on using smartphones for language documentation exist, but no product combines ambient wearable + auto-structured linguistic corpus + family viewing experience. |
| "Fire TV app endangered language stories India" | No existing Fire TV app found. Pratilipi (reading app) and Kuku FM (audio) exist on mobile only, and in major languages only. |

**Closest existing thing:** [Endangered Languages Project](https://www.endangeredlanguages.com/) by Google — a static web archive. No ambient capture, no structured NLP extraction, no family viewing experience. Also: [SayMore](https://software.sil.org/saymore/) by SIL — desktop software for organizing language recordings, but requires manual recording and annotation.

### Hackathon Fit
- **Highest scoring criterion:** Potential Impact (preserving dying languages = civilizational stakes) + Quality of Idea
- **Design:** Multi-surface experience — Bee captures → MCP structures → Fire TV displays
- **Tech Implementation:** Uses 3 Amazon products coherently

### 6-Day MVP Build Scope
1. **Day 1:** Set up Bee webhook receiver. Build MCP server skeleton with tools.
2. **Day 2–3:** Build `tag_linguistic_artifacts` tool — use spaCy + custom entity recognition for Indian proper nouns, kinship terms. Build `build_word_list` aggregation.
3. **Day 4:** Build Fire TV app (React Native for Vega OS or web-based) — episode list view + transcript playback with translated subtitles. Use AI image generation for story card illustrations.
4. **Day 5:** Integrate MCP server with Alexa+ for voice queries ("Alexa, play dadi's story about the river spirit").
5. **Day 6:** Record demo: show Bee capturing a mock elder conversation → backend extracts vocabulary + story → Fire TV shows the episode. Demo video script + submission.

---

## Concept 4: "SabhaSync" — Bee-Powered Real-Time Meeting Accountability for Indian Gram Panchayat & Society Meetings

### The Real-World Problem
**Who suffers:** Members of Indian housing societies (RWAs), gram panchayat meetings, and cooperative society meetings. Decisions are made verbally in chaotic group settings, minutes are written selectively (or not at all), office-bearers deny commitments, and ordinary members have no record of what was promised. In gram panchayats specifically, elected representatives make verbal promises to constituents that are never tracked.

**Why current solutions fail:**
- Otter.ai / Fireflies.ai are designed for Zoom/Teams corporate meetings, not noisy in-person Hindi/regional language group discussions
- Manual minute-taking is biased toward the secretary's interpretation
- No tool links ambient capture of a physical meeting → structured action items → public accountability dashboard
- No existing system tracks "promise vs. delivery" across multiple meetings

### Amazon Products Used (Technical Mechanism)
**Bee (primary) + Alexa+ MCP Server**

```
Society secretary or panchayat member wears Bee during physical meeting
  → Bee captures multi-speaker ambient conversation (Hindi/regional)
  → Structured output: transcript, speaker tags, action items, decisions

Your MCP Server:
  ├── Tool: extract_resolutions(session_id)
  │     → Parses transcript for decision patterns:
  │       "It was decided that...", "Secretary will...", "Budget approved for..."
  │     → Returns structured: {resolution, assigned_to, deadline, vote_count}
  ├── Tool: track_promise(person, promise, meeting_date)
  │     → Stores in SQLite/Supabase
  ├── Tool: get_accountability_report(person_or_committee)
  │     → "Ramesh ji promised road repair by Aug 15 — STATUS: Unfulfilled"
  │     → Tracks across meeting sessions
  └── Resource: meeting_minutes(meeting_id)
        → Auto-generated, timestamped, shareable minutes document

Alexa+ Interface:
  "Alexa, what did the secretary promise in last month's meeting?"
  → MCP calls get_accountability_report → Alexa reads out promises + status
  "Alexa, show society meeting minutes for September"
  → MCP Apps renders formatted minutes card
```

**Why Bee is ESSENTIAL:** Physical group meetings in noisy Indian settings (community halls, open-air panchayat sessions) can't be captured by Zoom transcription tools. Bee's ambient wearable form factor captures the entire session hands-free. Its speaker diarization + structured output pipeline is the core input.

### Novelty Verification

| Search performed | Result |
|---|---|
| "Bee wearable meeting minutes panchayat accountability" (Devpost) | No Devpost submissions found. |
| "gram panchayat meeting transcription AI India" | **⚠️ SabhaSaar** — government tool by Ministry of Panchayati Raj (launched Aug 2025, 1.1 lakh panchayats). Auto-generates minutes from audio recordings. BUT: it's a centralized government platform, not wearable-based, not for housing societies/RWAs, and has no cross-session promise tracking. |
| "housing society meeting minutes automation India" | MyGate, ApnaComplex, and ADDA track complaints and accounting, but none auto-transcribe physical meetings or track verbal promises. |

**Closest existing thing:** [SabhaSaar](https://pib.gov.in) (MoPR, 2025) — AI-powered meeting minutes for gram panchayats using BHASHINI. **Key differentiators of SabhaSync:** (1) Uses Bee wearable for ambient capture vs. SabhaSaar's manual audio upload, (2) targets housing societies/RWAs which SabhaSaar doesn't cover, (3) has a **cross-session promise accountability tracker** — SabhaSaar only generates single-meeting minutes. Also: [Fireflies.ai](https://fireflies.ai/) — Zoom/Teams only, no Hindi, no in-person meetings.

> [!WARNING]
> **Risk flag:** SabhaSaar's existence means judges may perceive panchayat meeting minutes as "already solved by the government." **Mitigation:** Position SabhaSync primarily for **housing society/RWA meetings** (SabhaSaar doesn't cover this) and emphasize the **promise-tracking-across-meetings** feature, which is genuinely novel.

### Hackathon Fit
- **Highest scoring criterion:** Potential Impact (governance transparency for 250K+ panchayats and millions of RWA meetings)
- **Quality of Idea:** "Promise tracker" is a genuinely novel framing
- **Tech Implementation:** Bee transcripts → NLP resolution extraction → cross-session promise tracking

### 6-Day MVP Build Scope
1. **Day 1:** Set up Bee integration, build MCP server skeleton.
2. **Day 2–3:** Build `extract_resolutions` tool — regex + LLM-based extraction of decision patterns from Hindi transcripts. Build promise database (SQLite).
3. **Day 4:** Build `get_accountability_report` — cross-session promise tracking with fulfillment status (manually tagged for MVP).
4. **Day 5:** Register Alexa+ add-on. Test voice queries for promise retrieval + meeting minutes.
5. **Day 6:** Record demo: show Bee capturing a mock society meeting → system extracts 3 resolutions → Alexa reports "Secretary promised plumbing fix by Oct 30 — unfulfilled." Video + submission.

---

## Concept 5: "DwarPal" — Ring + Alexa+ Intelligent Gate Sentry for Indian Homes (Package Theft, Delivery Verification, Domestic Worker Log)

### The Real-World Problem
**Who suffers:** Indian homeowners, especially in gated communities and independent houses, face a cluster of gate-level problems that Western Ring users don't encounter:
1. **Delivery disputes:** Amazon/Flipkart deliveries marked "delivered" but left with a neighbor or guard, with no photographic proof linked to the homeowner's own system
2. **Domestic worker time fraud:** Maid/cook/driver claims they came at 8 AM, left at 2 PM — no verifiable log
3. **Unauthorized visitor tracking:** Family wants to know who came while they were away — currently relies on unreliable guard registers
4. **Package pilferage in common areas:** Packages left at the gate get stolen before the homeowner returns

**Why current solutions fail:**
- Ring's motion alerts show "person detected" but don't identify *who* or *why* they're there
- MyGate (gated community app) requires guard participation and doesn't integrate with home cameras
- No system links doorbell press → identity recognition → automatic work-hour logging or delivery confirmation

### Amazon Products Used (Technical Mechanism)
**Ring API (primary) + Alexa+ MCP Server + MCP Apps**

```
Ring Doorbell detects person + doorbell press or motion
  → Webhook → Your backend:
      ├── Pull snapshot via Ring API
      ├── Face-match against registered roster:
      │     - Domestic workers (maid, cook, driver, gardener)
      │     - Regular delivery persons
      │     - Family members
      │     - Unknown → flag as visitor
      ├── Tool: log_worker_attendance(person_id, event_type, timestamp)
      │     → "Sunita (maid) — Arrived: 8:14 AM, Left: 1:47 PM"
      ├── Tool: verify_delivery(tracking_id_or_time_window)
      │     → Matches delivery timestamps with Ring motion events
      │     → Stores snapshot as proof: "Package arrived 3:22 PM, placed at gate"
      └── Tool: get_visitor_log(date_range)
            → List of all visitors with snapshots + timestamps

Alexa+ Interface:
  "Alexa, when did the maid come today?" → "Sunita arrived at 8:14 AM"
  "Alexa, was my Amazon package delivered?" → "Yes, at 3:22 PM. Here's the photo."
  "Alexa, who came while we were out?" → MCP Apps renders visitor gallery
```

**Why Ring is ESSENTIAL:** Ring's doorbell press event + snapshot API + WebRTC live view provide the raw signal. The face-matching and logging layer on top is the novel part. Without Ring's official webhook + per-device OAuth, you'd need a custom camera + motion detection + cloud storage pipeline — impractical for a hackathon.

### Novelty Verification

| Search performed | Result |
|---|---|
| "Ring doorbell domestic worker maid attendance tracking visitor log" (Devpost) | **⚠️ Partial overlaps found:** "Still Here" (Ring event history for household presence tracking), "Describe My Door" (Ring snapshot + vision model to describe visitors), "Ring Package Guardian" (webhook + Gemini Vision for doorstep activity timeline). None combine all 3 functions (worker attendance + delivery verification + visitor log) or target the Indian domestic-help context. |
| "smart doorbell maid attendance tracking" | No existing product combines doorbell events with worker attendance. TimeTapin, StaffAround, MaidCircle exist as standalone apps but don't use Ring data. |
| "Ring delivery verification proof snapshot" | Ring has "Package Detection" in some regions (US), but it's a simple motion zone — no identity linking, no attendance logging, no Alexa queryable history. |

**Closest existing thing:** ["Ring Package Guardian"](https://devpost.com) on Devpost — uses Ring webhooks + Supabase + Gemini Vision to log doorstep courier activity. **Key differentiators of DwarPal:** (1) Face-matching against a **registered domestic worker roster** for attendance tracking — no existing project does this, (2) combines delivery verification + worker attendance + visitor log in one system, (3) Alexa+ MCP queryable interface ("when did the maid come?").

> [!WARNING]
> **Risk flag:** Multiple Devpost projects use Ring webhooks + vision models for doorstep analysis. DwarPal's novelty rests specifically on the **domestic worker attendance** angle + **India-specific multi-persona UX**. In the demo video, lead with the attendance tracking — it's the unique differentiator.

### Hackathon Fit
- **Highest scoring criterion:** Design (cohesive multi-persona UX: homeowner, domestic worker, delivery verification) + Tech Implementation
- **Potential Impact:** Addresses daily friction for millions of Indian households
- **Quality of Idea:** Repurposes Ring as a household operations hub, not just security

### 6-Day MVP Build Scope
1. **Day 1–2:** Ring developer setup, OAuth flow, webhook receiver. Build face-matching pipeline using `face_recognition` Python library with a small registered roster (5–10 faces).
2. **Day 3:** Build MCP server with `log_worker_attendance`, `verify_delivery`, `get_visitor_log` tools.
3. **Day 4:** Register Alexa+ add-on. Build MCP Apps cards for visitor gallery and attendance summary.
4. **Day 5:** Test end-to-end with simulated Ring events (or real Ring doorbell if available). Handle edge cases (unknown face → "unrecognized visitor" alert).
5. **Day 6:** Record demo showing: maid arrives → Ring captures → Alexa reports attendance. Amazon delivery → Ring captures → Alexa confirms with photo. Video + README.

---

## Concept 6: "ParivaarTV" — Fire TV Elder-Companion App with Ring Visual Check-In + Alexa+ Family Dashboard

### The Real-World Problem
**Who suffers:** India has 15M+ elderly people living alone (Census 2021 projection). Adult children working in metros or abroad worry about aging parents in smaller cities. Current check-in methods: daily phone calls (parents sometimes don't answer or mask health issues), CCTV cameras (intrusive, parents feel surveilled), wearable panic buttons (elders forget to wear them or feel stigmatized).

**Why current solutions fail:**
- Dedicated elder-care apps (Emoha, Samarth) offer concierge services but no ambient monitoring
- CCTV in the home feels invasive and violates dignity
- Smartwatch fall detection requires daily charging and tech-savvy setup
- No system provides a *positive-signal* model: instead of alerting only on emergencies, it confirms "parent is active and well" throughout the day

### Amazon Products Used (Technical Mechanism)
**Fire TV (primary) + Ring API + Alexa+ MCP Server**

```
Parent's home setup:
  - Fire TV in living room (their TV)
  - Ring Indoor Cam in hallway/kitchen (common area only)
  - Echo/Alexa for voice interaction

Fire TV App ("ParivaarTV") runs on parent's TV:
  → Morning "Good Morning" routine: displays weather, medications, family photos
  → Parent presses a single remote button to send "I'm fine" signal
  → If no signal by 10 AM, system escalates

Ring Indoor Cam (common area):
  → Motion webhook → tracks activity patterns:
      "Last motion in kitchen: 7:45 AM" (parent made tea ✓)
      "No motion detected since 3 hours" → alert to child

MCP Server (child's Alexa+):
  ├── Tool: get_parent_status()
  │     → Aggregates: Fire TV "I'm fine" signal + Ring motion timeline
  │     → "Mom is active. Kitchen motion at 7:45 AM. Watched TV at 9:15 AM.
  │        Sent 'I'm fine' at 8:30 AM."
  ├── Tool: get_activity_pattern(date_range)
  │     → "Activity decreased 30% this week vs. last week" (early warning)
  ├── Tool: send_message_to_tv(message)
  │     → Pushes text/photo to parent's Fire TV screen
  └── Resource: family_photo_feed()
        → Rotating family photos on parent's TV screensaver

Child's Alexa+ query:
  "Alexa, how is Mom doing today?"
  → "Your mom sent her morning signal at 8:30 AM. She was active in the
     kitchen at 7:45 AM and watched TV until 10 AM. Activity is normal."
```

**Why Fire TV + Ring are ESSENTIAL:** Fire TV is the elder's *existing, familiar* TV interface — no new device adoption required. Ring's motion API provides *passive* activity sensing without intrusive recording. The combination creates a positive-signal system where the child gets reassurance, not just panic alerts.

### Novelty Verification

| Search performed | Result |
|---|---|
| "Fire TV app elderly monitoring parent India" | No existing Fire TV app for elder well-being monitoring. |
| "Ring camera elderly activity pattern tracking" | No Ring App Store product does activity-pattern analysis for elder care. Mercury Alert AI (Ring Appstore) does fall detection but not positive-signal daily well-being tracking. |
| "Alexa elderly care dashboard family" | Generic Alexa routines exist for reminders, but no MCP-based cross-device aggregation of Ring motion + Fire TV interaction into a family dashboard. |

**Closest existing thing:** [CarePredict](https://carepredict.com/) — wearable for elder activity tracking in senior living facilities. But it's institutional (not home-based), requires proprietary hardware, costs $300+/month, and doesn't integrate with Ring or Fire TV.

### Hackathon Fit
- **Highest scoring criterion:** Design (positive-signal dignity-preserving UX) + Potential Impact
- **Tech Implementation:** Uses 3 Amazon products (Fire TV app + Ring API + Alexa+ MCP) in a deeply integrated way
- **Quality of Idea:** Inverts the typical surveillance model into a reassurance model

### 6-Day MVP Build Scope
1. **Day 1–2:** Build Fire TV app (React Native for Vega OS) with morning routine screen + "I'm fine" button + photo carousel screensaver.
2. **Day 3:** Set up Ring API integration to capture motion events and build activity timeline (simple time-bucketed motion count).
3. **Day 4:** Build MCP server with `get_parent_status`, `get_activity_pattern`, `send_message_to_tv` tools.
4. **Day 5:** Register Alexa+ add-on for child's queries. Test the "no activity" escalation alert.
5. **Day 6:** Record demo: parent wakes up → kitchen motion logged → presses "I'm fine" on TV → child asks Alexa → gets reassuring report. Show "decreased activity" warning scenario. Video + submission.

---

## Concept 7: "JalVaani" — Alexa+ MCP Server for Municipal Water Supply Tracking & Complaint Filing in Indian Towns

### The Real-World Problem
**Who suffers:** Residents of Tier-2/3 Indian cities where municipal water supply arrives through pipelines for only 1–4 hours per day, at unpredictable times. When water doesn't arrive, residents must: (1) figure out if it's their ward or the whole zone, (2) call a municipal helpline that's perpetually busy, (3) arrange emergency tanker delivery at inflated prices, (4) file a complaint that goes into a black hole with no tracking.

This affects **100M+ households** in India where piped water is intermittent. Cities like Bengaluru, Hyderabad, Pune, Jaipur, and virtually every Tier-2 city face this daily.

**Why current solutions fail:**
- Municipal portals/apps (Mera Ration, CM Helplines) require smartphone navigation, reading ticket IDs, and filling forms
- IVRS helplines have 20+ minute wait times and no real-time supply status
- No system tells you "water is flowing in Zone 3 right now" based on community crowd-sourced data
- Government AI tools like ASHA (Anna Sahayata Holistic AI) focus on PDS/ration, not water supply

### Amazon Products Used (Technical Mechanism)
**Alexa+ MCP Server (primary)**

```
Resident has an Echo Dot or uses Alexa app on phone

Voice interaction:
  "Alexa, aaj paani kab aayega?"
  → MCP Server Tool: get_supply_schedule(ward="Shastri Nagar", zone="Zone 3")
  → "Zone 3 ka schedule hai subah 6–8 baje. Abhi 7:15 hai,
     3 neighbors ne report kiya paani aa raha hai."

  "Alexa, paani nahi aaya aaj"
  → MCP Server Tool: report_no_supply(ward, timestamp)
  → Adds to crowd-sourced outage map
  → "Noted. Aapke ward se 14 aur complaints hain aaj.
     Municipal complaint file karein? Haan bolein."

  "Haan"
  → MCP Server Tool: file_municipal_complaint(ward, issue="no_water_supply")
  → Generates complaint via municipal API/email/SMS gateway
  → "Complaint #WS-2026-4412 registered. Track status anytime — mujhse poochein."

  "Alexa, tanker ka rate kya hai aaj?"
  → MCP Server Tool: get_tanker_rates(area, capacity)
  → "5000 litre tanker: Shastri Nagar area mein ₹600–800.
     Verified supplier: Jal Suvidha, number 98xxxxxxxx."

MCP Apps Extension:
  → Ward-level outage heatmap (crowd-sourced)
  → Complaint tracking timeline
  → Historical supply reliability score per ward
```

**Why Alexa+ is ESSENTIAL:** The target user (middle-aged/elderly resident, often a homemaker managing household water) needs a voice interface — not another app to download. MCP's dynamic tool routing handles natural Hindi questions about water supply without rigid intents. The MCP Apps cards provide visual status that a family member can glance at on their phone.

### Novelty Verification

| Search performed | Result |
|---|---|
| "Alexa skill water supply tracking India municipal" (Devpost) | No Devpost submissions found. |
| "voice assistant water supply schedule India" | No existing product. Some IVRS helplines exist but are passive (wait on hold), not AI-powered or crowd-sourced. |
| "MCP server municipal utility complaint India" | No published MCP server for any Indian municipal utility. |
| "crowd-sourced water supply tracker India app" | [NextDrop](https://nextdrop.co/) was a Y-Combinator startup (2013–2017) that crowd-sourced water supply timing in Hubli-Dharwad and Bangalore. **It shut down.** No successor product exists. |

**Closest existing thing:** [NextDrop](https://nextdrop.co/) (defunct since ~2017) — SMS-based water supply alerts in Karnataka. Used valve operators to report when water was flowing. No voice interface, no AI, no complaint filing, no tanker marketplace. **The problem NextDrop identified remains entirely unsolved.**

### Hackathon Fit
- **Highest scoring criterion:** Quality of Idea (revives a proven problem statement with modern agentic architecture) + Potential Impact (100M+ households)
- **Tech Implementation:** MCP server with crowd-sourced reporting + municipal complaint generation + tanker marketplace lookup
- **Design:** Hindi-first, zero-friction reporting ("paani nahi aaya" → complaint filed in 2 voice turns)

### 6-Day MVP Build Scope
1. **Day 1–2:** Build MCP server (Python FastAPI + `mcp` SDK) with tools: `get_supply_schedule`, `report_no_supply`, `file_municipal_complaint`, `get_tanker_rates`. SQLite backend for crowd-sourced reports.
2. **Day 3:** Seed with sample ward/zone data for one city (e.g., Jaipur or Pune). Build crowd-sourced outage detection logic (if ≥5 reports from same ward in 2 hours → confirm outage).
3. **Day 4:** Register Alexa+ add-on. Build MCP Apps card for ward heatmap and complaint tracker.
4. **Day 5:** Municipal complaint filing via email/SMS gateway (or mock API for demo). Hindi response tuning.
5. **Day 6:** Record demo: resident reports no water → system confirms ward-level outage → files complaint → tracks status → shows tanker rate. Video + submission.

---

## Concept 8: "AnnaData" — Bee + Alexa+ MCP + AWS Bedrock AgentCore for Farmer Market Intelligence Agent (AWS Builder Track)

### The Real-World Problem
**Who suffers:** Indian smallholder farmers (86% of all farmers) who sell their produce at APMC mandis with zero information advantage. They don't know: (1) which mandi within 100km is offering the best price today, (2) whether prices are trending up (so they should hold) or down (so they should sell now), (3) what prices the *aadhtiya* (commission agent) quoted to other farmers 30 minutes ago — leading to systematic exploitation.

Farmers lose ₹4,000–8,000 per quintal on average due to information asymmetry with mandi agents (ICAR study, 2023).

**Why current solutions fail:**
- AGMARKNET (gov.in) publishes mandi prices but they're **previous-day prices**, not live, and require web navigation
- Existing Alexa skills for "Mandi Bhav" are simple read-aloud of AGMARKNET data — no cross-mandi comparison, no trend analysis, no real-time intelligence from conversations
- No system combines ambient conversational intelligence (what farmers are hearing at the mandi) with government price data for a real-time decision engine

### Amazon Products Used (Technical Mechanism)
**Bee (primary) + Alexa+ MCP Server + AWS Bedrock AgentCore (AWS Builder track qualifier)**

```
Farmer or local FPO coordinator wears Bee at the mandi
  → Bee captures ambient conversations with aadhtiya/traders:
      "Soybean ₹4,200 de rahe hain aaj"
      "Kal aur girega, aaj bech do"
  → Bee webhook pushes structured transcript to backend

Strands Agent (deployed on Bedrock AgentCore):
  ├── Tool: extract_price_signals(transcript)
  │     → NLP extracts: {commodity: "soybean", quoted_price: 4200,
  │        sentiment: "bearish", source: "trader_conversation"}
  ├── Tool: get_agmarknet_prices(commodity, state, date_range)
  │     → Fetches official AGMARKNET data for comparison
  │     → "Official modal price at Indore mandi: ₹4,350. Quoted: ₹4,200.
  │        Farmer is being offered ₹150 below modal price."
  ├── Tool: compare_nearby_mandis(commodity, location, radius_km=100)
  │     → "Ujjain mandi: ₹4,400 | Dewas: ₹4,280 | Indore: ₹4,350"
  ├── Tool: get_price_trend(commodity, days=7)
  │     → "Soybean prices ↑ 3.2% over last 7 days. Trend: bullish."
  └── AgentCore Memory: stores all price signals across sessions
        → Builds historical price intelligence per mandi

Alexa+ Interface (farmer queries from home before heading to mandi):
  "Alexa, soybean ka bhav kya hai aaj?"
  → "Indore mandi ₹4,350, Ujjain ₹4,400, Dewas ₹4,280.
     Last 7 days mein 3% upar gaya hai. Ujjain jaana better rahega."

  "Alexa, kal mandi mein kya sunaai diya?"
  → Pulls Bee transcript signals: "Traders were quoting ₹4,200,
     which is ₹150 below official modal price. Market sentiment was bearish
     but government data shows bullish trend."
```

**Why Bee + Alexa+ + AWS are ESSENTIAL:** Bee captures *real-time conversational intelligence* from the mandi floor — something no government database can provide. Alexa+ MCP makes it voice-accessible to a farmer who can't navigate AGMARKNET. AWS Bedrock AgentCore provides the agentic infrastructure to process, compare, and reason across multiple data sources (transcripts + AGMARKNET + trend analysis) autonomously.

### Novelty Verification

| Search performed | Result |
|---|---|
| "Alexa skill mandi price India" (Devpost) | Basic read-aloud skills exist (AGMARKNET data), but none combine ambient conversational intelligence + cross-mandi comparison + trend analysis. |
| "Bee wearable farmer mandi agriculture" | No results. Bee has never been used in agricultural contexts. |
| "crowd-sourced mandi price intelligence India" | No existing product. Some research papers on SMS-based price dissemination but no AI-powered live signal extraction. |
| "AWS Bedrock agent agriculture India hackathon" | No Devpost submissions combining Bedrock AgentCore with Indian agriculture + ambient capture. |

**Closest existing thing:** [Agridoot](https://agridoot.com/) and similar apps that display AGMARKNET prices. But they're passive data displays — no ambient capture, no conversational intelligence, no AI-powered "the trader is quoting below modal price" insight. Also: generic Alexa mandi-price skills exist but use hardcoded intents, not MCP architecture.

### Hackathon Fit
- **Highest scoring criterion:** Potential Impact (information asymmetry costs Indian farmers billions annually) + Tech Implementation (3 Amazon products + AWS services)
- **Quality of Idea:** Combines a wearable in a completely novel context (mandi floor intelligence gathering) with voice-first accessibility
- **AWS Builder mini-challenge qualifier:** Uses Strands SDK + Bedrock AgentCore for the agent backbone

### 6-Day MVP Build Scope
1. **Day 1:** Set up Bee webhook receiver. Build Strands agent skeleton with tool definitions. Set up Bedrock AgentCore project.
2. **Day 2:** Build `extract_price_signals` tool — LLM-based extraction of commodity, price, sentiment from Hindi/Hinglish transcripts.
3. **Day 3:** Build `get_agmarknet_prices` (scrape/API from data.gov.in) and `compare_nearby_mandis` tools. Seed data for MP/Rajasthan mandis.
4. **Day 4:** Deploy agent to Bedrock AgentCore. Register Alexa+ add-on for voice queries.
5. **Day 5:** Build MCP Apps card showing cross-mandi price comparison table + 7-day trend chart. Test end-to-end: Bee transcript → agent processes → Alexa reports.
6. **Day 6:** Record demo: FPO coordinator at mandi wearing Bee → hears trader quoting low → system flags "₹150 below modal" → farmer at home asks Alexa → gets recommendation to go to Ujjain mandi instead. Video + submission.

---

## Comparative Summary

| # | Concept | Products Used | Primary Track | AWS Bonus? | Novelty Confidence | Devpost Prior Art? | Impact Scope | Build Difficulty |
|---|---------|--------------|---------------|:---:|--------------------:|:---:|-------------|:---:|
| 1 | **NyayaSetu** | Alexa+ MCP | Alexa+ | ❌ | ★★★★★ | ✅ Clean | 800M+ underserved | Medium |
| 2 | **GaliGuard** | Ring + Alexa+ MCP | Ring | ❌ | ★★★★★ | ✅ Clean | Every Indian neighborhood | Medium-Hard |
| 3 | **VaniVault** | Bee + Fire TV + Alexa+ | Bee | ❌ | ★★★★★ | ✅ Clean | 197 endangered languages | Medium |
| 4 | **SabhaSync** | Bee + Alexa+ MCP | Bee | ❌ | ★★★★☆ | ⚠️ SabhaSaar (govt) exists for panchayats | 250K+ panchayats, millions of RWAs | Medium |
| 5 | **DwarPal** | Ring + Alexa+ MCP | Ring | ❌ | ★★★★☆ | ⚠️ Similar Ring projects on Devpost | Indian households with domestic help | Medium |
| 6 | **ParivaarTV** | Fire TV + Ring + Alexa+ | Fire TV | ❌ | ★★★★☆ | ⚠️ Generic elder care concepts exist | 15M+ elderly living alone | Medium-Hard |
| 7 | **JalVaani** | Alexa+ MCP | Alexa+ | ❌ | ★★★★★ | ✅ Clean (NextDrop is defunct) | 100M+ households | Easy-Medium |
| 8 | **AnnaData** | Bee + Alexa+ + AWS Bedrock | Bee + AWS | ✅ | ★★★★★ | ✅ Clean | 120M+ smallholder farmers | Medium-Hard |

> [!CAUTION]
> **~~KhataVoice~~ — DROPPED.** A very similar project called **"KiranaVoice"** was found on Devpost — voice-first AI credit ledger for kirana shops with Hinglish voice logging, split bills, and WhatsApp reminders. Building this would be duplicating existing work and judges may have already seen it.

---

## Devpost Novelty Scan Results (Oct 17, 2026)

| Concept | Devpost Search Performed | Threat Level | Action |
|---|---|:---:|---|
| NyayaSetu | "Alexa legal aid rural law India" | 🟢 None | "Nyaya Sahayak" exists but uses Gemini/LLaMA, not Alexa MCP |
| GaliGuard | "Ring camera stray animal cattle community alert" | 🟢 None | YOLO wildlife projects exist, none on Ring API |
| VaniVault | "Bee wearable endangered language preservation" | 🟢 None | No submissions found |
| SabhaSync | "Bee panchayat meeting minutes accountability" | 🟡 Moderate | SabhaSaar (govt tool) overlaps on panchayats. Pivot to RWA focus. |
| DwarPal | "Ring doorbell domestic worker maid attendance" | 🟡 Moderate | 3 similar Ring projects found. Lead with attendance angle. |
| ParivaarTV | "Fire TV elderly parent monitoring companion" | 🟡 Low-Moderate | Generic elder care concepts exist, none with this exact architecture |
| JalVaani | "Alexa water supply tracking India municipal" | 🟢 None | NextDrop (defunct 2017) was the only attempt |
| AnnaData | "Bee farmer mandi agriculture AWS Bedrock" | 🟢 None | Basic AGMARKNET skills exist, none with Bee + AgentCore |

---

## Strategic Recommendations

### If picking ONE concept to maximize winning probability:

1. **NyayaSetu** (Concept 1) — **strongest overall pick.** ★★★★★ novelty, zero Devpost prior art, highest social impact pitch, clean single-track build, compelling demo narrative. Access-to-justice angle is extremely strong for "Potential Impact" judging.

2. **JalVaani** (Concept 7) — **easiest build with strongest India-specific story.** Single product (Alexa+ MCP), clean demo, massive relatable impact. Every Indian will instantly understand "paani nahi aaya." NextDrop's failure and shutdown makes this a proven problem with no existing solution.

3. **GaliGuard** (Concept 2) — if you want the **most technically impressive Ring project.** Custom CV model + Ring API + Alexa+ MCP is a strong multi-product integration.

4. **AnnaData** (Concept 8) — if you want to **win the AWS Builder mini-challenge bonus** on top of the Bee track. Most complex build but hits 3 Amazon products + AWS services.

### Multi-track strategy
The hackathon allows submitting to multiple tracks. Best combo: **NyayaSetu** (Alexa+ track, clean impact story) + **GaliGuard** (Ring track, technical showcase) — they share no code and each is independently demonstrable. Add the **Open Source mini-challenge** by publishing your MCP server as a public GitHub repo with an open-source license — costs zero extra effort.

### AWS Builder bonus strategy
Any of the 8 concepts can qualify for the AWS Builder mini-challenge by deploying the MCP server backend on AWS (Lambda/EC2/ECS) and using Bedrock for LLM calls. AnnaData is designed for this from the ground up, but even NyayaSetu's RAG pipeline can use Bedrock + AgentCore for bonus points.

---

> [!IMPORTANT]
> **Simulated Alexa+ Web Experience:** The hackathon explicitly allows this — no Echo hardware needed. Use the Alexa+ developer console's testing interface to demonstrate your MCP server being called. For the demo video, screen-record the simulated web experience showing your tools being invoked.

> [!TIP]
> **Friction Log bonus:** Every track awards bonus points for a "Friction Log" documenting SDK/documentation pain points. Write one as you build — it costs nothing extra and directly influences the product teams.
