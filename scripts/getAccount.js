import {fetchToStr} from './lib';

async function getAccount() {
	let parser = new DOMParser();
	let doc = await fetchToStr('https://pw.mail.ru/usercp.php');

	doc = parser.parseFromString(doc, "text/html");

	return doc.getElementsByName('game_account')[0].value;
}

export {getAccount};