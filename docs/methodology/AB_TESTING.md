# Official A/B testing protocol

Complements [TEST_PROTOCOL.md](TEST_PROTOCOL.md). Required when changing preset JSON.

## Conditions

| Item | Requirement |
|------|-------------|
| Level match | Match **perceived** loudness first (use EasyEffects bypass + system volume), not just peak meters |
| Device | Same device + PipeWire quantum for both sides |
| Content | Same reference file region (±5 s cue) |
| Blind preferred | Hide preset names when possible |
| Duration | ≥ 20 s per excerpt; fatigue check at 15 min for heavy chains |

## Mandatory comparisons

For every candidate revision, compare against:

1. **Previous preset version** (git parent)
2. **Flat** (EasyEffects bypass / empty chain)
3. When relevant to category:
   - **FxSound** (Windows reference machine or recorded notes) — experimental / music-02 / cinema-02
   - **Dolby** OEM profile notes — movie / loudness
   - Category sibling (`*-01` vs `*-02`)

## Procedure

1. Load **A** (old) → score metrics → save log.
2. Load **B** (new) → score metrics → save log.
3. Optional: Flat baseline scores.
4. Fill [../../measurements/subjective/AB_TEMPLATE.md](../../measurements/subjective/AB_TEMPLATE.md).
5. Decide: **keep B** / **reject** / **iterate**.

## Decision rule

Keep B only if:

- Primary weighted metrics improve or hold, **and**
- No primary metric drops > 0.5 without explicit accepted trade-off, **and**
- Limiter still prevents audible overs on reference peaks.

## Documentation artefacts

| Artefact | Location |
|----------|----------|
| Subjective A/B | `measurements/subjective/` |
| Objective notes | `measurements/objective/` |
| Version rationale | `measurements/version-history/` |
| Datasheet update | `measurements/datasheets/` |
