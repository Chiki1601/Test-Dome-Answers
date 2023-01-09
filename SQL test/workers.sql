select items.name, sellers.name from items
join sellers on items.sellerId = sellers.id
where sellers.rating > 4;
