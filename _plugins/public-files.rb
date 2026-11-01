# Static assets are public only when explicitly listed. Private review notes,
# environment files and build tools must never be copied just because they exist.
Jekyll::Hooks.register :site, :post_read do |site|
  allowed = Array(site.config['public_assets'])
  site.static_files.select! { |file| allowed.include?(file.relative_path) }
end
