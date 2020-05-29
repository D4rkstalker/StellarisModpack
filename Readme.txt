[h1]Load Order[/h1]
Not important.

[h1]Older Versions[/h1]
[url=https://steamcommunity.com/sharedfiles/filedetails/?id=1885042831]For 2.3[/url]
[url=https://steamcommunity.com/sharedfiles/filedetails/?id=1897590680]For 2.4[/url]

[h1]Menu in action[/h1]
[img]https://media.giphy.com/media/LPlPcdqY1UsW0k8UII/giphy.gif[/img]

[h1]FAQ[/h1]

[i]What's the reasoning behind this?[/i]
Reasoning is that I wanted a "dynamic" mod GUI but couldn't find one. 

The only way for modders to create their own mod options menus are:
1. Using edict screen
2. Creating a custom button by overwriting a .gui file
3. Using Mod Menu mod

The only rather "dynamic" approach is using the edict screen. Others either have mod conflicts or require additional steps to be performed by third party developers.

[i]We already have a mod menu.[/i]
Yes, but it's not "dynamic".

[i]Is it truly a "dynamic" mod menu?[/i]
Nothing in this game can be truly "dynamic" but this mod menu gives an appearance of being "dynamic".

[i]What the hell do you mean "dynamic"?[/i]
This mod menu exposes 100 "slots" for other mods to "inject" as a button into this mod. 

Developers get to pick one unique Id (list will be kept somewhere which mods use which Id) and then:
1. Overwrite localization files related to this unique mod Id
2. Overwrite events related to this unique mod Id
3. Set a global flag related to this unique Id (comes via generated code)
4. Create own mod icon for the mod menu by overwriting a GFX resource related to this unique Id

[i]Only 100 slots?[/i]
Don't worry the code is auto generated (via script). If the limit is ever hit we can create more ids obviously.

[i]What's the advantage of this approach?[/i]
- Mod developers don't have to message back and forth (Mod Menu maintainer and XYZ mod developer)
- Create compatibility patches for custom buttons
- Mods don't clutter the edicts menu

Almost zero communication between myself and mod developers is necessary (only if you require support probably). I don't need to do anything in order for your mod menu button to show here. Only thing mod developers need to do is let everyone know which mod Id they've taken.

[i]What files are overwritten?[/i]
main_bottom.gui

[i]Some other mod that I use already overwrites main_bottom.gui.[/i]
Let me know which so I can create a patch. Other developers are welcome to create patches themselves as well.

[i]Menu icon is not showing.[/i]
It's probably a mod conflict. See above.

[i]Are there any existing compatibility patches?[/i]
[url=https://steamcommunity.com/workshop/filedetails/discussion/1840010432/2564160288800825062/]Here[/url]

[i]Mod icon is terrible.[/i]
I know and that's not a question.

[i]Can I create my own mod icon for this?[/i]
Yes of course. You can send it to me to include in the mod (credits will be given) or create your own mod override. Whatever suits you is fine by me.

[i]I found a typo or grammar error.[/i]
Great. Let me know what the error is and where exactly and post a correction so I can update the localization file.

[i]I don't like this mod![/i]
Don't install it then.

[i]Is this mod required to be installed?[/i]
If the mod developer who pointed you here implemented the overrides via provided python script then it should not be a dependency. You can use whatever alternate method is present to launch the mod UI that you installed.

[i]Help, Mod Id conflicts with another mod.[/i]
Please ask the mod author to change the selected mod Id.

[i]Achievements compatible? Ironman compatible?[/i]
I don't care about Achievements or Ironman so assume all my mods are not compatible.

[i]I want to make a menu for my mod.[/i]
Here's a python script which can generate bare bones code for you: https://pastebin.com/5ZTRhHd0
If you need an actual sample message me and I'll use the following tool to generate one for you.

[i]As a mod developer what can I customize?[/i]
Button look on the menu, text on the menu. 

Once the menu button is clicked control is transferred to your own dmm event. You can do what you want with it (in the override). Relaunch your own menu, replace whole code. 

I only recommend that you add somewhere 
[code]remove_global_flag = dmm_mod_<mod_id>_opened[/code]
in your close options event code. In the sample it is added in after block.

[i]How can I check if DMM is installed?[/i]
[code]has_global_flag = dynamic_mod_menu_installed[/code]