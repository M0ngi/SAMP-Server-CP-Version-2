#include <a_samp>
#include <Dini>

#define COLOR_RED 0xFF0000FF

#if !defined isnull
    #define isnull(%1) ((!(%1[0])) || (((%1[0]) == '\1') && (!(%1[1]))))
#endif

public OnFilterScriptInit()
{
	print("----------------------------------------------------");
	print(" Server Control Panel executable - By Mongi ");
	print("----------------------------------------------------");
	SetTimer("FileChecker", 1000, true);
	
	new File: file = fopen("/CPFolder/ChatLog.txt", io_append);
	fwrite(file, "Server Starts...");
	fclose(file);
	
	print("Timer Started!");
	return 1;
}

public OnFilterScriptExit()
{
	return 1;
}

public OnPlayerText(playerid, text[])
{
	new File: file = fopen("/CPFolder/ChatLog.txt", io_append);
	new pName[MAX_PLAYER_NAME], string[256];
	GetPlayerName(playerid, pName, sizeof(pName));
	format(string, sizeof(string), "\n%s[%d]: %s", pName, playerid, text);
	fwrite(file, string);
	fclose(file);
	return 1;
}

forward FileChecker();
public FileChecker()
{
	if(dini_Exists("/CPFolder/ControlPanel.cfg"))
	{
	    new user_name[MAX_PLAYER_NAME];
	    if(dini_Isset("/CPFolder/ControlPanel.cfg", "KickPlayer"))
	    {
			format(user_name, sizeof(user_name), "%s", dini_Get("/CPFolder/ControlPanel.cfg", "KickPlayer"));
		}
		else if(dini_Isset("/CPFolder/ControlPanel.cfg", "BanPlayer")){
		    format(user_name, sizeof(user_name), "%s", dini_Get("/CPFolder/ControlPanel.cfg", "BanPlayer"));
		}
		for(new id=0 ; id < MAX_PLAYERS ; id++)
		{
		    if(isnull(user_name)) break;
		    if(IsPlayerConnected(id))
		    {
		        new pName[MAX_PLAYER_NAME];
		        GetPlayerName(id, pName, sizeof(pName));
		        if(strcmp(user_name, pName) == 0) // Match
		        {
		            print("Found");
		            if(dini_Isset("/CPFolder/ControlPanel.cfg", "KickPlayer"))
				    {
						SendClientMessage(id, COLOR_RED, "You've been kicked by an offline admin from the server.");
                        SetTimerEx("PlayerBanKick", 1000, false, "ii", id, 0); // Kick
					}
					else{
					    SendClientMessage(id, COLOR_RED, "You've been banned by an offline admin from the server.");
					    SetTimerEx("PlayerBanKick", 1000, false, "ii", id, 1); // Ban
					}
					dini_Remove("/CPFolder/ControlPanel.cfg");
					break;
		        }
		    }
		}
	}
	return 1;
}

forward PlayerBanKick(usrid, ans);
public PlayerBanKick(usrid, ans)
{
	if(ans) // Ban = 1
	{
		Ban(usrid);
	}
	else{ // Kick = 0
		Kick(usrid);
	}
	return 1;
}

