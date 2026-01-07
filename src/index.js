require('dotenv').config();
const { Client, GatewayIntentBits } = require('discord.js');
const axios = require('axios');

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
  ],
});

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('messageCreate', async (msg) => {
  if (msg.content === '!new') {
    try {
      const response = await axios.post(`${process.env.API_BASE_URL}/servers/${msg.guild.id}/tickets`, {
        title: 'New Ticket',
        description: 'A new ticket has been created.',
        user_id: msg.author.id,
      });
      msg.reply(`Ticket created with ID: ${response.data.ticket_id}`);
    } catch (error) {
      console.error(error);
      msg.reply('Failed to create ticket.');
    }
  }
});

client.login(process.env.DISCORD_TOKEN);
