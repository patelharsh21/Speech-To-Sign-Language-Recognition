const recordButton = document.getElementById('record-btn');
const outputArea = document.getElementById('output');

let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

recordButton.addEventListener('click', () => {
	recognition.start();
});

recognition.onresult = (event) => {
	const speechToText = event.results[0][0].transcript;
	outputArea.innerHTML += speechToText;
}

recognition.onerror = (event) => {
	console.error(event.error);
}
