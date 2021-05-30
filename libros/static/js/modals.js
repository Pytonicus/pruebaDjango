document.addEventListener('DOMContentLoaded', ()=>{
    var botones = document.getElementsByClassName('md-btn');
    var parrafo = document.getElementById('parrafoEliminar');
    var link = document.getElementById('linkAModal');
    var cabecera = document.getElementById('tituloEditar');
    
     // Formulario:
     var portadaForm = document.getElementsByClassName('portadaForm');
     var tituloForm = document.getElementsByClassName('tituloForm');
     var autorForm = document.getElementsByClassName('autorForm');
     var categoriasForm = document.getElementsByClassName('categoriasForm');
     var idForm = document.getElementById('idForm');

    for(let i = 0; i < botones.length; i++){
        botones[i].addEventListener('click', ()=>{
            let id = botones[i].getAttribute('data-id');
            let titulo = botones[i].getAttribute('data-titulo');
            let autor = botones[i].getAttribute('data-autor');
            let categorias = botones[i].getAttribute('data-categorias');
            console.log(`ID: ${id}, Título: ${titulo}`);
            link.href = 'borrar/' + id;
            parrafo.innerHTML = titulo;
            cabecera.innerHTML = "Editar: " + titulo;
            // formulario:
            tituloForm[1].value = titulo;
            
            for(let i = 0; i < autorForm[1].length; i++){
                if(autorForm[1].options[i].text == autor){
                    autorForm[1].options[i].selected = true;
                }
            }

            try{
                let categoria = categorias.split(',');

                for(let i = 0; i < categoriasForm[1].length; i++){
                    for(let cat in categoria){
                        if(categoriasForm[1].options[i].text == categoria[cat]){
                            categoriasForm[1].options[i].selected = true;
                        }
                    }
                }
            }catch(e){
                
            }

            idForm.value = id;
        });
    }



});