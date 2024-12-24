// Lazy Loading for Older Messages
const chatMessages = document.getElementById('chat-messages');
chatMessages.addEventListener('scroll', () => {
  if (chatMessages.scrollTop === 0) {
    const loading = document.querySelector('.loading');
    loading.style.display = 'block';
    setTimeout(() => {
      loading.style.display = 'none';
      chatMessages.innerHTML =
        `<div class="message user"><p>Older message loaded.</p><span class="time">9:55 AM</span></div>` +
        chatMessages.innerHTML;
    }, 1500);
  }
});

// Emoji Picker Toggle
const emojiPicker = document.getElementById('emoji-picker');
document.querySelector('.emoji-picker-button').addEventListener('click', () => {
  emojiPicker.classList.toggle('active');
});

emojiPicker.addEventListener('click', (event) => {
  if (event.target.tagName === 'SPAN') {
    const textarea = document.querySelector('.chat-input textarea');
    textarea.value += event.target.textContent;
  }
});

// File Attachment
document.querySelector('.attach-button').addEventListener('click', () => {
  alert('File attachment feature is under development!');
});
