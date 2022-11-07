package nl.meister.minecraftPlugin;

import org.bukkit.plugin.java.JavaPlugin;

public class TutorialPlugin extends JavaPlugin {
    @Override
    public void onEnable() {
        getServer().getPluginManager().registerEvents(new pluginListener(), this);
        getLogger().info("onEnable is called!");
    }

    public void onDisable() {
        getLogger().info("onDisable is called!");
    }
}
