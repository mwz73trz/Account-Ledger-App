const BASE_URL = "http://localhost:8000/";

const getInit = () => {
  return {
    headers: {
      "Content-Type": "application/json",
    },
  };
};

const tryCatchFetch = async (url, init) => {
  try {
    let response = await fetch(url, init);
    if (response.ok) {
      if (response.status !== 204) {
        let data = response.json();
        return data;
      } else {
        return { success: true };
      }
    }
  } catch (error) {
    console.error(":ERR:", error);
    return null;
  }
};

const getLedgers = async () => {
  let url = `${BASE_URL}api/ledgers/`;
  return await tryCatchFetch(url, getInit());
};

const getLedgerById = async (ledgerId) => {
  let url = `${BASE_URL}api/accounts/${ledgerId}/`;
  return await tryCatchFetch(url, getInit());
};

const myExports = {
  getLedgers,
  getLedgerById,
};

export default myExports;
