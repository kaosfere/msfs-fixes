# G1000 Improved

This is a beta released of an improved G1000 for the new Microsoft Flight Simulator.  It's the next step up from the various tweaks I'd previously released allowing pilots to control G1000 brightness with hardware knobs in their cockpits.  I figured, rather than work around the absence of software dimming in the G1000, why not just add that feature to the display itself?   That's what this is.  Each panel is now individually dimmable from within the PFD configuration menu.

This menu I had to create from scratch, and it approximates what it looks like in real life, but isn't exact, for two reasons.  One, I omitted the AUTO/MANUAL switch because auto brightness makes no sense in the sim right now.  Two, I don't own a G1000 or a G1000 simulator, so I had to go off a few small images and fuzzy videos.  I got it pretty close using what I had available in the sim without taking ages to get it pixel-perfect.  I think it works, but I'm open to suggestions for improvements.  (Or gifts of a G1000 simulator. :) )

If you want to see this in action, I have put a brief [video on YouTube](https://www.youtube.com/watch?v=vZExvOiBZNw).

I also added functionality to toggle synthetic vision on and off, a feature that's in the real units that are equipped with synthetic vision but which is also missing from the sim.

Installation for this is the same as for any mod, just dump it into your Community folder.  I don't necessarily plan on stopping here and may be making further tweaks to the G1000.  I'm open to suggestions.  The latest version of this can always be found [at github](https://github.com/kaosfere/msfs-fixes/tree/master/rcj-g1000) and I welcome bug reports or suggestions there.

There two things to note:

* If you have my previous DA40 or DA62 lighting tweaks installed you can remove those.  They're no longer need with this mod, and won't work with it anyway.
* This _will_ disable the control of G1000 brightness via the avionics knob in the Cessna 172 G1000 (and any others that have it).  If that's an issue for enough folks I can release compatibility tweaks for those in the future.
  
Finally, I need to give credit to [dga711](https://github.com/dga711), whose [devkit](https://github.com/dga711/msfs-webui-devkit) mod made working on this practical, and to the folks at the [A320 Neo project](https://github.com/wpine215/msfs-a320neo/), who let me know that it exists.  Their project is a lot more ambitious than mine, you should check it out.
