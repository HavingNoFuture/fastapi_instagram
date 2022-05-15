import $ from "jquery";

/**
 * Конвертирует форму в json
 * @param {string} form - Селектор формы
 * @return {JSON} json
 */
export function convertFormToJSON(form) {
    const array = $(form).serializeArray(); // Encodes the set of form elements as an array of names and values.
    const json = {};
    $.each(array, function() {
      json[this.name] = this.value || "";
    });
    return json;
}