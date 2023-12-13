// reference: https://getbootstrap.com/docs/5.0/components/modal/
// for showing vocab details
var vocabModal = document.getElementById('vocabModal')
vocabModal.addEventListener('show.bs.modal', function (event) {

    var button = event.relatedTarget

    var vocabWord = button.getAttribute('vocabWord')
    var vocabMeaning = button.getAttribute('vocabMeaning')
    var vocabExample = button.getAttribute('vocabExample')
    var vocabFamiliarity = button.getAttribute('vocabFamiliarity')

    var modalTitle = vocabModal.querySelector('.modal-title')
    vocabModal.querySelector('.modal-body #vocabModal-vocabMeaning').innerHTML = '<b>Meaning:</b> ' + vocabMeaning
    vocabModal.querySelector('.modal-body #vocabModal-vocabExample').innerHTML = '<b>Example:</b> ' + vocabExample
    vocabModal.querySelector('.modal-body #vocabModal-vocabFamiliarity').innerHTML = '<b>Familiarity:</b> ' + vocabFamiliarity

    modalTitle.innerHTML = 'Vocab Info <br>@' + vocabWord
})