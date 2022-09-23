function WorkerLogOut(url) {
    Swal.fire({
        title: 'Are you sure?',
        text: "Would you like to finish your sesion?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#e74a3b',
        cancelButtonColor: '#4e73df',
        confirmButtonText: 'Log out!'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = url
        }
    })
}