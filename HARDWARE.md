# SD Hexpansion

![A hexagonal PCB with MicroSD card socket](./sdhexpansion.png)

A Hexpansion for the [EMFCamp Tildagon badge](https://tildagon.badge.emfcamp.org/) which adds a MicroSD card socket in SPI mode.  The Hexpansion has an 8kB EEPROM and has a load switch for the SD card (there are a bunch of reasons SD cards can get "stuck" and are only recoverable by power cycling).

## Design files

This board was designed in open-source tool [KiCad](https://www.kicad.org/) which is available for
anyone to download and use to modify this design.  The board was then turned into a panel so that it
could be maufactured 4 at a time to reduce costs and wasted PCB material (without the panel the board
would not have been big enough for the automatic assembly machines and a wasted panel would have been
added).

The design for the single part is in `sdhexpansion.kicad_pro`.  Once this was complete and passing ERC a panel was created using [KiKit](https://github.com/yaqwsx/KiKit), the configuration for this is in sdhexpansion-panel.json.  The resulting KiCad board file is the `sdhexpansion-panel.kicad_pcb`.  The manufacturing files for JLCPCB were generated from the panel file using KiKit on the cli:

    kikit fab jlcpcb --no-drc --assembly --schematic sdhexpansion.kicad_sch sdhexpansion-panel.kicad_pcb sdhexpansion_v1

The manufacturing files are in `sdhexpansion_v1` folder.  These files are all for the 2x2 panel, so if you upload and order 5 you get 20 boards etc.
