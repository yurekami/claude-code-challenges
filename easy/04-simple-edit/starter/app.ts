// Application main file
import { helper } from './utils';

interface Data {
  id: number;
  name: string;
  value: number;
}

interface Item {
  id: string;
  type: string;
}

// Bug: should be userName
const usrName = 'John';

// Bug: should return Promise<Data>
async function getData(): any {
  const response = await fetch('/api/data');
  return response.json();
}

// Bug: item should have type Item
function processItem(item) {
  console.log(`Processing ${item.id}`);
  return {
    ...item,
    processed: true
  };
}

async function main() {
  const data = await getData();
  console.log(`Hello, ${usrName}`);
  console.log(`Data: ${JSON.stringify(data)}`);
}

main();
