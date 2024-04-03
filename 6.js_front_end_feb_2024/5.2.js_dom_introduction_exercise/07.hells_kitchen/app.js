function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);
 
   function onClick () {
      let input = document.querySelector('#inputs textarea').value
      let restourants = [];
      for (const el of JSON.parse(input)) {
         let [name, workersString] = el.split(" - ")
         let workers = [];
         for (const worker of workersString.split(", ")) {
            let [name, salary] = worker.split(" ")
            workers.push({name, salary: Number(salary)})
         }
         if (restourants.some(restourant => restourant.name === name)) {
            let currentRestourant = restourants.find(restourant => restourant.name === name)
            for (const worker of workers) {
               currentRestourant.workers.push(worker)
            }
         } else {
            restourants.push({name, workers})
         }
         
      }
      let bestRestourantName = "";
      let bestAverageSallary = Number.MIN_SAFE_INTEGER;
      let bestWorkerSallary = 0;
      let bestWorkersList = [];
 
      for (const restourant of restourants) {
         let sallarySum = 0;
         let currentBestSallary = Number.MIN_SAFE_INTEGER;
         for (const worker of restourant.workers) {
            sallarySum += worker.salary
            if (worker.salary > currentBestSallary) {
               currentBestSallary = worker.salary
            }
         }
 
         let currentAverageSallary = sallarySum / restourant.workers.length
         if (currentAverageSallary > bestAverageSallary) {
            bestRestourantName = restourant.name
            bestAverageSallary = currentAverageSallary
            bestWorkerSallary = currentBestSallary
            bestWorkersList = restourant.workers.sort((a, b) => b.salary -a.salary)
         }
      }
      let bestWorkerListFinal = [];
      for (const worker of bestWorkersList) {
         bestWorkerListFinal.push(`Name: ${worker.name} With Salary: ${worker.salary}`)
      }
      document.querySelector('#bestRestaurant p').textContent = `Name: ${bestRestourantName} Average Salary: ${bestAverageSallary.toFixed(2)} Best Salary: ${bestWorkerSallary.toFixed(2)}`
      document.querySelector('#workers p').textContent = bestWorkerListFinal.join(" ")
   }
}