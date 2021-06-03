const url = window.location.href
const quizBox = document.getElementById("quiz-box")
const modalBody = document.getElementById('modal-body-confirm')
let no_qs = null
$.ajax({
   type: 'GET',
   url: `${url}data`,
   success: function (response) {
      data = response.data
      no_qs = data.length
      data.forEach(el => {
         for (const [qs, ans] of Object.entries(el)) {
            quizBox.innerHTML += `
             <hr>
             <div class="mb-2">
             <b>${qs}</b>
             </div>`
            ans.forEach(a => {
               quizBox.innerHTML += `
             <div>
                <input type="radio" class="ans" id="${qs}-${a}" name="${qs}" value="${a}">
                <label for="${qs}">${a}</label>
            </div>
             `
            })
         }
      })

      const quizForm = document.getElementById('quiz-form')
      const csrf = document.getElementsByName("csrfmiddlewaretoken")
      const elements = [...document.getElementsByClassName("ans")]

      function submit_quiz() {
         data = {}
         data['csrfmiddlewaretoken'] = csrf[0].value
         elements.forEach(el => {
            if (el.checked) {
               data[el.name] = el.value
            } else {
               if (!data[el.name]) {
                  data[el.name] = null
               }
            }
         })

         $.ajax({
               type: 'POST',
               url: `${url}submit/`,
               data: data,
               success: function (response) {
                  const modal_header = document.getElementsByClassName("modal-header")
                  let is_pass = null
                  if (response.pass == true) {
                     is_pass = "Congratulations..!!"
                     $(modal_header).addClass("bg-success")
                  } else {
                     is_pass = "Better Luck Next Time"
                     $(modal_header).addClass("bg-danger")
                  }
                  modalBody.innerHTML = `
                           <div class="h5"><b>${response.quiz_name}</b><div>
                           <div class="text-muted">
                           <ul>
                           <li>No of questions: <b>${no_qs}</b></li>
                           <li>Correct Ans: <b>${response.correct_ans}</b></li>
                           <li>Wrong Ans: <b>${response.wrong_ans} %</b></li>
                           <li>Score: <b>${response.earned_score} %</b></li>
                           </ul>
                           </div>
                           <div class="h5 col-12 text-center"><b>${is_pass}</b><div>
                    `
               }, error: function (error) {
                  console.log(error)
               }
            }
         )
      }

      quizForm.addEventListener('submit', event => {
         event.preventDefault()
         submit_quiz()
      })

   },
   error: function (error) {
      console.log(error)
   }
})
