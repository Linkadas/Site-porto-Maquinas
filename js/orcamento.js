document.addEventListener('DOMContentLoaded', () => {
    const selectEl = document.getElementById('interesse-select');
    if (!selectEl) return;

    // A lista de equipamentos foi injetada estaticamente no HTML
    // para funcionar sem a necessidade de servidor (file:///).
    // Apenas inicializamos a biblioteca Choices.js para busca:
    
    if (window.Choices) {
        new Choices(selectEl, {
            searchEnabled: true,
            itemSelectText: '',
            noResultsText: 'Nenhum equipamento encontrado',
            noChoicesText: 'Sem opções disponíveis',
            shouldSort: false, // Mantém a ordem da página original
            placeholder: true,
            placeholderValue: 'Selecione um equipamento',
            searchPlaceholderValue: 'Buscar equipamento...'
        });
    }
});
