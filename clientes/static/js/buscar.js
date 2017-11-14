function buscar() {
  // Declare variables
  var input, filter, table, tr, td, i;
  input = document.getElementById("un_cliente");
  filter = input.value.toUpperCase();
  table = document.getElementById("tabla_clientes");
  tr = table.getElementsByTagName("tr");
  
  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

var cuil;
function devolver_cuil(fila) {  // devuelve el cuil de la fila seleccionada
  var traer_cliente;
  cuil= fila.getElementsByTagName("td")[0].innerHTML;
  traer_cliente= {"cuil":cuil};
  var cliente_json= JSON.stringify(traer_cliente);
  document.getElementById("demo").innerHTML= cliente_json;
  return cuil;
}

