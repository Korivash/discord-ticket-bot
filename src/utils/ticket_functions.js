// src/utils/ticket_functions.js

async function createTicket(interaction) {
    // Implement ticket creation logic here
    const channel = await interaction.guild.channels.create(`ticket-${interaction.user.username}`, {
        type: 'GUILD_TEXT',
        permissionOverwrites: [
            {
                id: interaction.user.id,
                allow: ['VIEW_CHANNEL', 'SEND_MESSAGES', 'READ_MESSAGE_HISTORY'],
            },
            {
                id: interaction.guild.roles.everyone.id,
                deny: ['VIEW_CHANNEL'],
            },
        ],
    });

    await channel.send(`Welcome to your ticket, ${interaction.user}!  How can we help you today?`);
    await interaction.reply({ content: `Ticket created: ${channel}`, ephemeral: true });
}

module.exports = { createTicket };