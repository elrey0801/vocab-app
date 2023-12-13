// reference: https://getbootstrap.com/docs/5.0/components/modal/
// for updating vocab
var changeVocabModal = document.getElementById('changeVocabModal')
changeVocabModal.addEventListener('show.bs.modal', function (event) {

    var button = event.relatedTarget

    var vocabWord = button.getAttribute('vocabWord')
    var vocabMeaning = button.getAttribute('vocabMeaning')
    var vocabExample = button.getAttribute('vocabExample')
    var modalTitle = changeVocabModal.querySelector('.modal-title')
    changeVocabModal.querySelector('.modal-body #changeVocabModal-vocabWord').value = vocabWord
    changeVocabModal.querySelector('.modal-body #changeVocabModal-vocabMeaning').value = vocabMeaning
    changeVocabModal.querySelector('.modal-body #changeVocabModal-vocabExample').value = vocabExample

    modalTitle.innerHTML = 'Vocab Edit <br>@' + vocabWord
    changeVocabModal.setAttribute('vocabFamiliarity', button.getAttribute('vocabFamiliarity'))
    changeVocabModal.setAttribute('vocabId', button.getAttribute('vocabId'))
})