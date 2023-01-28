import {getPromoItemsDoc, getAccInfo} from './lib';
import {allowed} from "./allowed";

async function sendGifts() {
	let doc = await getPromoItemsDoc();
	let acc = getAccInfo(doc, allowed ? allowed : {byId: {}, all: []});

	if (acc === null)
		return 'Подарки не переданы. Ошибка получения информации об аккаунте: неверно указан сервер или никнейм персонажа';
	else if (acc === -1)
		return 'Все распакованные подарки уже переданы';

	let items = doc.getElementsByName('cart_items[]');
	let res = '';

	for (let i = 0; i < items.length; i++) {
		res += '&cart_items%5B%5D=' + items[i].value;
	}

	await fetch(`https://pw.mail.ru/promo_items.php?do=process${res}&acc_info=${acc}`);

	return 'Подарки переданы';
}

await sendGifts();