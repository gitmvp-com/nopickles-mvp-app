// Conversation history
let messages = [];

// Load menu on page load
document.addEventListener('DOMContentLoaded', () => {
    loadMenu();
    
    // Allow Enter key to send message
    document.getElementById('user-input').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});

// Load menu items from API
async function loadMenu() {
    try {
        const response = await fetch('/api/menu');
        const menu = await response.json();
        
        const menuItemsContainer = document.getElementById('menu-items');
        menuItemsContainer.innerHTML = '';
        
        // Display menu items
        for (const [item, price] of Object.entries(menu.prices)) {
            const menuItem = document.createElement('div');
            menuItem.className = 'menu-item';
            menuItem.innerHTML = `
                <div class="menu-item-name">${item}</div>
                <div class="menu-item-price">$${price.toFixed(2)}</div>
            `;
            menuItemsContainer.appendChild(menuItem);
        }
    } catch (error) {
        console.error('Error loading menu:', error);
    }
}

// Send message to the API
async function sendMessage() {
    const input = document.getElementById('user-input');
    const messageText = input.value.trim();
    
    if (!messageText) return;
    
    // Add user message to UI
    addMessage('user', messageText);
    
    // Clear input
    input.value = '';
    
    // Add to conversation history
    messages.push({ role: 'user', content: messageText });
    
    // Disable send button
    const sendBtn = document.getElementById('send-btn');
    sendBtn.disabled = true;
    sendBtn.textContent = 'Thinking...';
    
    try {
        // Call API
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ messages })
        });
        
        if (!response.ok) {
            throw new Error('Failed to get response');
        }
        
        const data = await response.json();
        
        // Add assistant message to UI
        addMessage('assistant', data.message);
        
        // Add to conversation history
        messages.push({ role: 'assistant', content: data.message });
        
    } catch (error) {
        console.error('Error sending message:', error);
        addMessage('assistant', '❌ Sorry, I encountered an error. Please make sure you have set your OpenAI API key in the .env file.');
    } finally {
        // Re-enable send button
        sendBtn.disabled = false;
        sendBtn.textContent = 'Send';
        input.focus();
    }
}

// Add message to chat UI
function addMessage(role, content) {
    const chatMessages = document.getElementById('chat-messages');
    
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}-message`;
    
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    
    if (role === 'assistant') {
        messageContent.innerHTML = `<strong>NoPickles Assistant:</strong><p>${content}</p>`;
    } else {
        messageContent.innerHTML = `<p>${content}</p>`;
    }
    
    messageDiv.appendChild(messageContent);
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
