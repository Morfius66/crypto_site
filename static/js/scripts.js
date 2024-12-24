function updateCryptoPrices() {
    fetch('/api/crypto-data')
        .then(response => response.json())
        .then(data => {
            data.forEach(coin => {
                // Обновление цены
                document.getElementById(`price-${coin.id}`).textContent = `$${coin.current_price.toFixed(2)}`;

                // Обновление изменения цены
                const changeElement = document.getElementById(`change-${coin.id}`);
                changeElement.textContent = `${coin.price_change_percentage_24h.toFixed(2)}%`;
                changeElement.className = coin.price_change_percentage_24h >= 0 ? 'text-success' : 'text-danger';
            });
        })
        .catch(error => console.error('Ошибка при обновлении данных:', error));
}

// Обновление каждые 5 секунд
setInterval(updateCryptoPrices, 5000);
