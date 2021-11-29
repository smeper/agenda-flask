const btnDelete = document.querySelectorAll('.btn-delete')

if (btnDelete) {
    const lista = Array.from(btnDelete)
    lista.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Quieres eliminarlos')){
                e.preventDefault();
            }
        })
    })
}