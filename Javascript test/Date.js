function formatDate(userDate) {
  const x = userDate.split('/');
  return `${x[2]}${x[1]}${x[0]}`;
}

console.log(formatDate("12/31/2014"));
