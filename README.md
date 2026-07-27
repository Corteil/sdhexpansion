# SD Hexpansion

![A hexagonal PCB with MicroSD card socket](./sdhexpansion.png)

A Hexpansion for the [EMFCamp Tildagon badge](https://tildagon.badge.emfcamp.org/) which adds a MicroSD card socket in SPI mode.  The Hexpansion has an 8kB EEPROM and has a load switch for the SD card (there are a bunch of reasons SD cards can get "stuck" and are only recoverable by power cycling).  Details of the hardware design can be found in [the hardware docs](HARDWARE.md).

## Using your SD Hexpansion

To make use of the hexpansion right away without writing any of your own code, get an micro SD card
and plug it into a computer.  The card needs to be formatted as a FAT filesystem, that's what most
cards will be.

1. Make a folder on the SD card called `sdcard_apps`
2. Inside this folder you can place standard [Tildagon apps](https://tildagon.badge.emfcamp.org/tildagon-apps/)
3. Safely remove the SD card from your computer
4. Plug it into your hexpansion
5. Power up the badge
6. The hexpansion app for your SD card reader should pop up with three menu items "Mount", "Remove" and "Format".  Select the "Mount" option then exit the app (button F on the badge front-panel).
7. Now look at the bottom of the list of apps on the launcher, the apps on your SD card should be there and ready to go!

### Why "sdcard_apps"?
There's a [bug in micropython](https://github.com/emfcamp/badge-2024-software/issues/334) which means that `import` doesn't work properly if it includes the mount point of a FAT filesystem.  To work around this the driver EEPROM adds the mount-point (`sdcard` which is the name of the folder on the badge where all the files on your card will appear) to the system path.  That means that when `import` is run it searches in the SD card for micropython code.  If the folder where all the apps were installed on the SD card was just called `apps` it would have the same name as the default location on the badge itself and the software wouldn't know which of the two `apps` folders to look in.  The paths discussed here aren't magic, they are all defined in the EEPROM app which is run when the hexpansion is plugged in.

## Driver EEPROM

### Driver Hacking

If you want to modify the code that is in the driver app, you will need to follow the steps
here to get the modified code onto the hexpansion.

To squeeze the most out of the 8kB EEPROM on the hexpansion I've been compiling to
a `*.mpy` file, I've done this already but if you want to modify it you'll need to
do this step.  You need the [mpy-cross](https://pypi.org/project/mpy-cross/) tool
then you can simply run

    mpy-cross app.py

To setup a blank SD Hexpansion you need to plug it in to your badge and connect to the badge using [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html).

On the host change into the `app` directory of a checkout of this repository and run:

    mpremote mount .

This will connect to the running micropython system on your badge, hit `Ctrl-C` to
interrupt the normal OS and get a Python prompt.  Make sure the SDHexpansion is in port 2 (the right hand side) and short out the write-protect pins to allow the EEPROM to be overwritten (I normally use a pair of tweezers, but a jumper wire or even a bent paperclip will probably do).  Then on the mpremote terminal type:

    import prepare_eeprom

And that's it, the code runs on import and should have set up the EEPROM and copied the app.  Reboop the badge and you should get a new app offering to let you "Mount", "Remove" or "Format" the SD card.
