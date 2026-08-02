# Calibration — Realtek

Onboard Realtek codec paths (ALC*). Primary migrant target from Windows OEM stacks.

## Procedure

1. Register device under `validation/hardware/` or `measurements/hardware/`.
2. Set PipeWire baseline (48 kHz).
3. Bypass OEM DSP if possible.
4. Run [TEST_PROTOCOL](../../docs/methodology/TEST_PROTOCOL.md) + [AB_TESTING](../../docs/methodology/AB_TESTING.md).
5. Store results in `validation/logs/` with hardware ID.

## Linked campaign device

HW-001 Acer Nitro (Realtek ALC255) lives under Notebook + Realtek classes.
