function addEvent() {
  const date = document.getElementById("event-date").value;
  const title = document.getElementById("event-title").value;
  if (!date || !title) return;

  const events = JSON.parse(localStorage.getItem("events") || "[]");
  events.push({ date, title });
  localStorage.setItem("events", JSON.stringify(events));
  renderEvents();
}

function renderEvents() {
  const events = JSON.parse(localStorage.getItem("events") || "[]");
  const list = document.getElementById("event-list");
  list.innerHTML = "";
  events.forEach((event, index) => {
    const li = document.createElement("li");
    li.textContent = `${event.date}: ${event.title}`;
    list.appendChild(li);
  });
}

renderEvents();
