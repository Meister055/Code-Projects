package nl.meister.minecraftPlugin;

import org.bukkit.Bukkit;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.event.EventHandler;
import org.bukkit.event.EventPriority;
import org.bukkit.event.player.AsyncPlayerChatEvent;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.event.Listener;
import org.bukkit.event.server.ServerCommandEvent;
import org.bukkit.entity.Player;

public class pluginListener implements Listener {
    @EventHandler (priority = EventPriority.LOW)
    public void onPlayerJoin(PlayerJoinEvent event){
        Bukkit.broadcastMessage("Welcome to the rice fields motherfucker!");
    }
    @EventHandler (priority = EventPriority.NORMAL)
    public void onChat(AsyncPlayerChatEvent event) {
        String eventMessage = event.getMessage();
        Player eventPlayer = event.getPlayer();

        Bukkit.broadcastMessage(String.format("Player: %s, Message: %s", eventPlayer.getName(), eventMessage));

        if (eventMessage.equals("Let there be light!")){
            Bukkit.dispatchCommand(CommandSender.getName());
        }

        if (eventMessage.equals("Who am I?")){
            Bukkit.broadcastMessage(String.format("You are %s!", eventPlayer.getName()));
        }

    }

}
