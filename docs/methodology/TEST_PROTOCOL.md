# Official preset test protocol

Version: **1.0** · Applies to every new or revised preset before merge.

## 1. Install

1. Branch from `main`.
2. Install preset via `./scripts/install.sh` or UI import.
3. Confirm plugin list matches documentation.
4. Set PipeWire to a known baseline (48 kHz, quantum 1024) unless testing latency specifically.

## 2. Reference playback

Play material from [../../references/](../../references/) matching the preset category (minimum **3** items).

## 3. Evaluation dimensions

Score each **1–5** (1=poor, 5=excellent) and write qualitative notes:

| Dimension | Question |
|-----------|----------|
| Voice / dialog | Are words intelligible without harshness? |
| Bass | Tight vs muddy? Speaker strain? |
| Treble / air | Clear vs fatiguing? |
| Stereo image | Wide but stable center? |
| Soundstage | Depth impression without phase mess? |
| Explosions / peaks | Controlled by limiter? Pumping? |
| Compression | Natural glue or squashed? |
| Listening fatigue | After 15–20 minutes? |

## 4. Record observations

Use [../../measurements/LOG_TEMPLATE.md](../../measurements/LOG_TEMPLATE.md):

- Date, EasyEffects version, device, PipeWire quantum
- Preset name + git commit
- Scores + free-form notes
- Pass / fail / iterate

## 5. Compare to previous version

A/B with the last tagged preset revision (bypass toggle or dual presets).  
Reject changes that win one dimension but collapse two others without documented trade-off.

## 6. Automation baseline

```bash
./scripts/validate.sh
python3 scripts/check_markdown_links.py
```

JSON validity is necessary but **never sufficient** — listening is mandatory for DSP changes.
