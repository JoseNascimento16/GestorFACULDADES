// $(document).ready(function(){
//     console.log('entrou disabled')
//     $('#formNotas').submit(function(){
//         $("#formNotas :disabled").removeAttr('disabled');
//     });
// })

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('#formNotas').addEventListener('submit', function() {
    Array.from(this.querySelectorAll(":disabled")).forEach(element => element.removeAttribute("disabled"));
    });
});

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('#formDisciplinas').addEventListener('submit', function() {
    Array.from(this.querySelectorAll(":disabled")).forEach(element => element.removeAttribute("disabled"));
    });
});

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('#formAlunos').addEventListener('submit', function() {
    Array.from(this.querySelectorAll(":disabled")).forEach(element => element.removeAttribute("disabled"));
    });
});
    
    
    
    
    