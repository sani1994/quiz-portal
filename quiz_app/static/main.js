const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-btn')

let modaldata = {}
const url = window.location.href

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
   modaldata['pk'] = modalBtn.getAttribute('data-pk'),
      modaldata['quiz'] = modalBtn.getAttribute('data-quiz'),
      modaldata['question'] = modalBtn.getAttribute('data-question'),
      modaldata['difficulty'] = modalBtn.getAttribute('data-difficulty'),
      modaldata['time'] = modalBtn.getAttribute('data-time'),
      modaldata['pass'] = modalBtn.getAttribute('data-pass'),
      modaldata['topic'] = modalBtn.getAttribute('data-topic')

   modalBody.innerHTML = `
      <div class="h5 mb-3">Are you sure to start "<b>${modaldata.quiz}</b>" ?<div>
      <div class="text-muted">
      <ul>
      <li>Difficulty: <b>${modaldata.difficulty}</b></li>
      <li>No of questions: <b>${modaldata.question}</b></li>
      <li>Time: <b>${modaldata.time}</b></li>
      <li>Pass: <b>${modaldata.pass} %</b></li>
      </ul>
      </div>
        `
   if (parseInt(modalBtn.getAttribute('data-question')) !== 0) {
      startBtn.addClass('hide')
   }
   startBtn.addEventListener('click', () => {
      window.location.href = url + modaldata.pk

   })

}))
