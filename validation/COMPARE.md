# Technical comparison — Flat vs category presets

Hardware reference: HW-001 · EasyEffects 8.2.8 · evidence: UI screenshots + JSON topology.

| Dimension | Flat (bypass) | Cinema (`cinema-01/02`) | Music HD (`music-hd-01/02`) | Gaming (`gaming-01/02`) | Voice Boost | FxSound Ultimate |
|-----------|---------------|-------------------------|-----------------------------|-------------------------|-------------|------------------|
| Processing | None | EQ + bass + dyn + lim | EQ + exciter (+ heavy stack on 02) | Presence EQ + dyn | Mid-forward speech chain | Full enhancer stack |
| Loudness | Source | 01 mild / 02 Autogain −18 | 01 mild / 02 Autogain −20 | 01 mild / 02 Autogain −19 | 01 makeup / 02 Autogain −21 | Autogain −18 |
| Bass | Source | Enhancer present | 01 none / 02 enhancer | Controlled enhancer | 01 cut lows / 02 mild | Strong enhancer |
| Width | Source | 01 none / 02 stereo tools | Mild / enhanced | Mild / enhanced | Minimal | Wide |
| Primary goal | Reference | Dialog + immersion | Fidelity / playlist glue | Positioning / immersion | Intelligibility | Wow / laptop speakers |
| Seal (VC-2026-08) | n/a | Beta | Beta | Beta | Beta | Experimental |

## Topology sketches

```text
Flat:                 App ─────────────────────────────► Device

cinema-01:            EQ → Bass → Comp → Limiter
cinema-02:            AG → MB → EQ → Exc → Bass → ST → Lim

music-hd-01:          EQ → Exc → ST → Lim
music-hd-02:          AG → MB → EQ → Exc → Bass → ST → Lim

gaming-01:            EQ → Bass → ST → Comp → Lim
gaming-02:            AG → MB → EQ → Exc → Bass → ST → Lim

voice-boost-01:       EQ → Gate → Comp → De-esser → Lim
voice-boost-02:       AG → MB → EQ → Exc → Bass → ST → Lim

fxsound-ultimate-02:  AG → MB → EQ → Exc → Bass → ST → Lim
volume-booster-01:    EQ(+2 flat) → Comp → Lim
```

## How to compare on your machine

Follow [../docs/methodology/AB_TESTING.md](../docs/methodology/AB_TESTING.md) using Flat bypass as A0 and each preset as B.
