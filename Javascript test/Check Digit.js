/**
 * @prop {string} membershipId: The customer's membership ID.
 * @return {number} The check digit.
 */
function createCheckDigit(membershipId) {
  let sumMembershipId = aggregator(membershipId);
  while (parseInt(sumMembershipId) > 9) sumMembershipId = aggregator(sumMembershipId);
  return sumMembershipId;
}

function aggregator(strMembershipId) {
  return strMembershipId.toString().split('').reduce((a, b) => parseInt(a) + parseInt(b), 0);
}

console.log(createCheckDigit("55555"));
