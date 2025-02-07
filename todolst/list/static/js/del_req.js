function del(id) {
       fetch(`/todo/${id}/`, {
           method: 'DELETE',
           headers: {
               'Content-Type': 'application/json',
           }
       })
       .then(response => {
           if (response.ok) {
               if (response.status === 204) {
                   console.log('Task deleted successfully, no content returned');
                   return null;
               } else {
                   return response.json();
               }
           } else {
               throw new Error(`HTTP error! Status: ${response.status}`);
           }
       })
       .then(data => {
           if (data) {
               console.log('Success:', data);
           }
           location.reload();
       })
       .catch((error) => {
           console.error('Error:', error);
       });
   }

export {del}