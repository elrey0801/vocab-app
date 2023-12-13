// reference: https://getbootstrap.com/docs/5.0/components/modal/
// for updating vocabSetName
var changeVocabSetNameModal = document.getElementById('changeVocabSetNameModal')
    changeVocabSetNameModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    var vocabSetName = button.getAttribute('vocabSetName')

    var modalTitle = changeVocabSetNameModal.querySelector('.modal-title')
    var modalBodyInput = changeVocabSetNameModal.querySelector('.modal-body #vocabSetNewName')

    modalTitle.innerHTML = 'New VocabSet name for <br>@' + vocabSetName
    modalBodyInput.value = vocabSetName
    modalBodyInput.setAttribute('vocabSetId', button.getAttribute('vocabSetId'))
})