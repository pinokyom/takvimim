function saveNote() {
  const note = noteText.value.trim();
  const done = doneCheckbox.checked;

  fetch(`/notes/${selectedDate}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ note, done })
  }).then(() => {
    generateCalendar();
    closeModal();
  });
}

function openModal(date) {
  selectedDate = date;
  modalDate.textContent = `Not: ${date}`;

  fetch(`/notes/${selectedDate}`)
    .then(res => res.json())
    .then(data => {
      noteText.value = data.note || '';
      doneCheckbox.checked = data.done || false;
      modal.style.display = 'block';
    });
}
