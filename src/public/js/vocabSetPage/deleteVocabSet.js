// reference: https://getbootstrap.com/docs/5.0/components/modal/
// for deleting VocabSet
var deleteVocabSetModal = document.getElementById('deleteVocabSetModal')
deleteVocabSetModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget

    var vocabSetId = button.getAttribute('vocabSetId')
    var vocabSetName = button.getAttribute('vocabSetName')

    var modalTitle = deleteVocabSetModal.querySelector('.modal-title')

    deleteVocabSetModal.querySelector('.modal-body #deleteVocabSetModal-vocabSetName').innerHTML = '<b>Delete VocabSet:</b> ' + vocabSetName

    deleteVocabSetModal.setAttribute('vocabSetId', vocabSetId)
})