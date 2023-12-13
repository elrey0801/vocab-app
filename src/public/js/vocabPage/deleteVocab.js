// reference: https://getbootstrap.com/docs/5.0/components/modal/
// for deleting vocab
var deleteVocabModal = document.getElementById('deleteVocabModal')
deleteVocabModal.addEventListener('show.bs.modal', function (event) {

    var button = event.relatedTarget

    var vocabId = button.getAttribute('vocabId')
    var vocabWord = button.getAttribute('vocabWord')
    var vocabMeaning = button.getAttribute('vocabMeaning')
    var vocabExample = button.getAttribute('vocabExample')

    var modalTitle = deleteVocabModal.querySelector('.modal-title')
    deleteVocabModal.querySelector('.modal-body #deleteVocabModal-vocabMeaning').innerHTML = '<b>Meaning:</b> ' + vocabMeaning
    deleteVocabModal.querySelector('.modal-body #deleteVocabModal-vocabExample').innerHTML = '<b>Example:</b> ' + vocabExample

    modalTitle.innerHTML = 'Delete Vocab <br>@' + vocabWord
    deleteVocabModal.setAttribute('vocabId', vocabId)
})