---
name: itaca
description: Legacy ARM, mobile, embedded, and PC hardware preservation, Board Support Package (BSP) analysis, Device Tree (DTB/DTS) reconstruction, HAL/driver interoperability, and mainline Linux/OpenWrt/postmarketOS/LineageOS porting via REA.
---

# ITACA :: LEGACY HARDWARE PRESERVATION & MAINLINE BSP MODERNIZATION

## 0. SCOPE & STATUTORY INTEROPERABILITY
- **Purpose**: Extend the usable lifecycle of user-owned End-of-Life (EoL) ARM smartphones, tablets, single-board computers (SBCs), routers, and legacy PCs that no longer receive manufacturer software updates.
- **Compliance Basis**:
  - **EU Directive 2009/24/EC Art. 6 & Recital 15**: Hardware/software interface documentation and decompilation strictly necessary to achieve interoperability between an independently created operating system/driver and existing hardware components.
  - **EU Right-to-Repair & Ecodesign Framework**: Preventing premature hardware obsolescence through open-source firmware and OS portability.
  - **GPLv2 Compliance**: Reconciling vendor Linux kernel binary modules (`.ko`) and boot images with mainline Linux kernel trees.

---

## 1. LEGACY ARM & DEVICE MODERNIZATION WORKFLOW (`/goal` LOOP)

```text
WHILE (unmapped_peripherals > 0 || dtb_warnings > 0 || kernel_boot != PASS || hal_interfaces_broken > 0):
  1. INVENTORY hardware SoC, bootloader, partitions, and peripheral buses.
  2. EXTRACT Device Tree (DTB), kernel config, vendor HALs, and firmware blobs.
  3. DOCUMENT register maps, GPIO/pinctrl, clocks, regulators, and IPC protocols via REA.
  4. SYNTHESIZE clean mainline Device Tree (.dts), user-space daemon, or portable driver.
  5. VERIFY boot, peripheral initialization, and power management on target hardware.
```

---

## 2. REA TOOL DISPATCH FOR HARDWARE & BSP RECOVERY

### A. FIRMWARE, BOOT IMAGE & PARTITION EXTRACTION
- `inspect_firmware_regions` -> `extract_firmware`: Locate and unpack `boot.img`, `vendor_boot.img`, `dtbo.img`, `super.img`, `initramfs`, U-Boot images, FIT images, and SquashFS/EXT4/EROFS root filesystems.
- `inspect_artifact` -> `extract_artifact`: Extract ramdisks, vendor firmware blobs (`/lib/firmware/*`), and board configuration archives.
- `list_architectures` / `inspect_binary_layout`: Identify exact instruction set architecture (`ARMv7-A`, `AArch64`, `MIPS`, `RISC-V`, `x86_64`), endianness, and load addresses.

### B. DEVICE TREE (DTB/DTS) & BOARD TOPOLOGY RECONSTRUCTION
1. Extract compiled Flattened Device Tree (`.dtb`) from boot image or running device (`/sys/firmware/fdt`).
2. Decompile via `dtc -I dtb -O dts -o board.dts board.dtb`.
3. Cross-reference MMIO base addresses, interrupt numbers (`GIC`), `pinctrl` states, `i2c`/`spi` bus nodes, `regulator-fixed`/`pmic` rails, and `dsi`/`panel` timing tables against vendor kernel modules using REA static analysis (`open_binary`, `list_strings`, `xrefs`).

### C. VENDOR KERNEL MODULE (`.ko`) & HAL INTERFACE ANALYSIS
- **Static Inspection**: `open_binary` -> `list_procedures`, `list_strings`, `batch_decompile`, `procedure_pseudo_code`, `inspect_native_data_type`.
- **Target Artifacts**:
  - Vendor kernel modules (`*.ko`): Extract `of_device_id` compatible strings, `regmap` configurations, `ioctl` command numbers, and initialization sequences.
  - Android/Linux HAL shared libraries (`hardware/*.so`, `libhybris`, HIDL/AIDL services, V4L2/ALSA/DRM/Mesa bridges): Map exported symbol tables (`list_names`), IPC message structures, and shared-memory ring buffers.
  - Windows-on-ARM / Legacy PC drivers (`*.sys`, `*.dll`): Use `inspect_pe_resources`, `inspect_native_load_image`, and `procedure_pseudo_code` to document ACPI/UEFI hardware descriptors and translate them into Linux mainline Device Tree or ACPI tables.

### D. AUTHORIZED DIAGNOSTICS ON OWNED DEVICES (ADB / SERIAL / GDB / FRIDA)
- **Android / Linux Device Bridge**: `list_adb_devices` -> `inspect_adb_device`, `list_adb_features`, `list_adb_services`, `read_adb_logcat`, `collect_adb_bugreport`, `pull_adb_file` (for reading `/proc/cpuinfo`, `/proc/iomem`, `/proc/interrupts`, `/sys/kernel/debug/clk/clk_summary`, `/sys/kernel/debug/gpio`).
- **Hardware Bus & Signal Verification**: `inspect_signal_decoders` -> `decode_signal_recording` to validate UART boot logs, I2C sensor initialization, SPI display panels, and USB descriptors (`libusb` / `hidapi`).
- **Runtime Interface Tracing**: `observe_native_calls`, `instrument_with_frida`, `start_gdb_session` on user-owned test devices to record exact parameter values passed between user-space services and vendor HALs.

### E. CLEAN-ROOM DRIVER & MAINLINE PORTING SYNTHESIS
1. **Obligation Ledger**: Record every hardware subsystem (SoC clock/reset, storage eMMC/UFS/NVMe, Wi-Fi/BT SDIO/PCIe, display DRM/KMS, audio ALSA/ASoC, battery/PMIC, sensors IIO) in `build_reconstruction_obligation_ledger`.
2. **Mainline Target Synthesis**:
   - **postmarketOS / Mainline Linux Mobile**: Generate clean `.dts`/`.dtsi` files, `APKBUILD` device packages, `uci` or `udev` rules, and `alsa-ucm-conf` profiles.
   - **LineageOS / AOSP**: Generate `BoardConfig.mk`, `device.mk`, `proprietary-files.txt`, SELinux policy rules (`sepolicy`), and AIDL/HIDL compatibility shims.
   - **Armbian / OpenWrt / Debian ARM**: Generate U-Boot board defconfigs, mainline DTS overlays, and user-space peripheral daemons (`libusb`/`hidapi`/`i2c-dev`).
3. **Verification**: Validate coverage via `evaluate_reconstruction_coverage` and `verify_reconstruction`.
