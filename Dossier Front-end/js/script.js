document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');
    const jobListingsContainer = document.getElementById('job-listings');
    const loadingIndicator = document.getElementById('loading');
    const noResultsMessage = document.getElementById('no-results');

    // Fonction pour charger les offres d'emploi (simulée)
    async function fetchJobs(keywords = '', location = '') {
        loadingIndicator.classList.remove('hidden');
        jobListingsContainer.innerHTML = ''; // Effacer les résultats précédents
        noResultsMessage.classList.add('hidden');

        // Simuler une requête API (à remplacer par l'appel à ton backend)
        await new Promise(resolve => setTimeout(resolve, 1500)); // Simuler un délai

        const mockJobs = [
            { id: 1, title: 'Développeur Python Senior', company: 'Entreprise XYZ', location: 'Abidjan, Côte d\'Ivoire', date: '2025-04-15' },
            { id: 2, title: 'Ingénieur Cybersécurité Python', company: 'SecureTech Africa', location: 'Treichville', date: '2025-04-10' },
            { id: 3, title: 'Data Scientist Python', company: 'Analytics IA', location: 'Télétravail', date: '2025-04-05' },
            // ... plus d'offres simulées
        ];

        loadingIndicator.classList.add('hidden');

        const filteredJobs = mockJobs.filter(job =>
            job.title.toLowerCase().includes(keywords.toLowerCase()) &&
            job.location.toLowerCase().includes(location.toLowerCase())
        );

        if (filteredJobs.length > 0) {
            filteredJobs.forEach(job => {
                const jobCard = document.createElement('div');
                jobCard.className = 'bg-white shadow rounded-md p-6 hover:shadow-lg transition duration-300';
                jobCard.innerHTML = `
                    <h3 class="text-xl font-semibold text-indigo-600 mb-2">${job.title}</h3>
                    <p class="text-gray-700 mb-2"><i class="fas fa-building mr-2"></i> ${job.company}</p>
                    <p class="text-gray-700 mb-2"><i class="fas fa-map-marker-alt mr-2"></i> ${job.location}</p>
                    <p class="text-gray-700 text-sm">Publié le ${new Date(job.date).toLocaleDateString()}</p>
                    <a href="/offre/${job.id}" class="inline-block bg-indigo-200 text-indigo-700 py-2 px-3 rounded-full text-sm mt-4 hover:bg-indigo-300">
                        <i class="fas fa-eye mr-2"></i> Voir l'offre
                    </a>
                `;
                jobListingsContainer.appendChild(jobCard);
            });
        } else {
            noResultsMessage.classList.remove('hidden');
        }
    }

    // Écouter la soumission du formulaire de recherche
    if (searchForm) {
        searchForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const keywordsInput = document.getElementById('keywords');
            const locationInput = document.getElementById('location');
            fetchJobs(keywordsInput.value, locationInput.value);
        });

        // Charger toutes les offres au chargement de la page (simulé)
        fetchJobs();
    }
});
