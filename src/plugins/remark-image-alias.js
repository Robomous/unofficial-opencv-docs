import { visit } from 'unist-util-visit';
import { fileURLToPath } from 'url';
import { dirname, relative, resolve } from 'path';

/**
 * Remark plugin to handle image path aliases in markdown
 * Allows using @assets/ shortcut instead of relative paths
 * 
 * Usage in markdown:
 * ![Alt text](@assets/images/image.webp)
 * 
 * This will be converted to the correct relative path based on the file location
 */
export default function remarkImageAlias() {
	return (tree, file) => {
		if (!file || !file.path) return;
		
		try {
			// Get the directory of the current markdown file
			let fileDir;
			if (typeof file.path === 'string') {
				if (file.path.startsWith('file://')) {
					fileDir = dirname(fileURLToPath(file.path));
				} else {
					// Already a file system path
					fileDir = dirname(file.path);
				}
			} else {
				return; // Skip if path is not a string
			}
			
			// Path to src/assets from project root
			const projectRoot = resolve(process.cwd());
			const assetsPath = resolve(projectRoot, 'src/assets');
			
			visit(tree, 'image', (node) => {
				// Handle @assets/ alias
				if (node.url && typeof node.url === 'string' && node.url.startsWith('@assets/')) {
					try {
						// Remove the @assets/ prefix
						const imagePath = node.url.replace('@assets/', '');
						// Resolve the full path to the image
						const fullImagePath = resolve(assetsPath, imagePath);
						// Calculate relative path from the markdown file to the image
						const relativePath = relative(fileDir, fullImagePath);
						// Use forward slashes (works on all platforms)
						let normalizedPath = relativePath.replace(/\\/g, '/');
						
						// Normalize the path - ensure it's a valid relative path
						// If the path doesn't start with . or /, make it relative
						if (!normalizedPath.startsWith('.') && !normalizedPath.startsWith('/')) {
							normalizedPath = './' + normalizedPath;
						}
						
						// Validate: ensure the path is valid (not empty, not absolute in wrong way)
						if (normalizedPath && normalizedPath.length > 0 && !normalizedPath.startsWith('/')) {
							node.url = normalizedPath;
						} else {
							throw new Error(`Invalid path generated: ${normalizedPath}`);
						}
					} catch (err) {
						// Fallback: use a simple relative path calculation
						// Count how many directories deep from src/content/docs
						const pathParts = fileDir.split(/[/\\]/);
						const docsIndex = pathParts.findIndex(p => p === 'docs');
						if (docsIndex >= 0) {
							// Count levels from docs/ to current file directory
							const levelsDeep = pathParts.length - docsIndex - 2; // -2 for 'docs' and the section folder
							const upLevels = '../'.repeat(levelsDeep + 1); // +1 to get to src/ level
							node.url = upLevels + 'assets/' + imagePath;
						} else {
							// Ultimate fallback: assume we're 2 levels deep (fundamentals/)
							node.url = '../../assets/' + imagePath;
						}
					}
				}
			});
		} catch (error) {
			// If path resolution fails, silently skip to avoid breaking the build
			// The @assets/ paths will remain unchanged and might cause issues, but won't break routing
		}
	};
}
