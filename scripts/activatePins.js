import {getAccount} from './getAccount';

async function activatePins(pins = []) {
	if (pins.length === 0)
		return;

	const account = await getAccount();

	if (account)
		pins.forEach(async (pin) => {
			await fetch(`https://pw.mail.ru/pin.php?do=activate&pin=${pin}&game_account=${account}`);
		})
}

const pins = arguments[0];

await activatePins(pins);