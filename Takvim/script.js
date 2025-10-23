function saveNote() {
  const note = noteText.value.trim();
  const done = doneCheckbox.checked;

  fetch(`https://takvim-api.onrender.com/notes/${selectedDate}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ note, done })
  }).then(() => {
    generateCalendar();
    closeModal();
  });
}
