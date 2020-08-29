# MSFS package builder

This python script is a quick utility which will take a skeletonized `layout.json` file and update it with the correct file size and timestamp using the correct [Windows filetime format](https://docs.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-filetime).  It currently does not seem to matter much if your size or times are correct, as long as the file name is right, but it might matter at some point, and why not do something right if you can?

This code has *not* been rigorously tested on an environment outside of my Ubuntu/WSL workstation and may break elsewhere.  Try it and let me know.