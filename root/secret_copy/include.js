const _xai_rand_ = '_' + Math.random().toString(36).slice(2);
const _xai_params_ = new URLSearchParams(window.location.search);
const _xai_file_ = _xai_params_.keys().next().value;
if (!_xai_file_) {
  console.error('No file specified in query parameter');
} else {
  const _xai_pass_ = prompt('Enter decryption password for ' + _xai_file_);
  if (_xai_pass_) {
    fetch(_xai_file_ + '.enc')
      .then(_xai_res_ => {
        if (!_xai_res_.ok) throw new Error('File not found');
        return _xai_res_.arrayBuffer();
      })
      .then(_xai_data_ => {
        const _xai_iv_ = new Uint8Array(_xai_data_.slice(0, 16));
        const _xai_cipher_ = new Uint8Array(_xai_data_.slice(16));
        const _xai_key_ = CryptoJS.enc.Utf8.parse(_xai_pass_.padEnd(32).slice(0, 32));
        const _xai_dec_ = CryptoJS.AES.decrypt(
          { ciphertext: CryptoJS.lib.WordArray.create(_xai_cipher_) },
          _xai_key_,
          { iv: CryptoJS.lib.WordArray.create(_xai_iv_) }
        );
        const _xai_text_ = _xai_dec_.toString(CryptoJS.enc.Utf8);
        if (!_xai_text_) throw new Error('Decryption failed');
        eval(`(function ${_xai_rand_}(){${_xai_text_}})();`);
      })
      .catch(_xai_err_ => console.error('Error:', _xai_err_.message));
  }
}
