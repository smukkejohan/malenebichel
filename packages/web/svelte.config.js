//import preprocess from 'svelte-preprocess';
import vercel from '@sveltejs/adapter-vercel';
import { vitePreprocess } from '@sveltejs/kit/vite';


export default {

  preprocess: vitePreprocess(),

  kit: {
    adapter: vercel({
      runtime: 'edge',

      // an array of dependencies that esbuild should treat
      // as external when bundling functions
      external: [],

      // if true, will split your app into multiple functions
      // instead of creating a single one for the entire app
      split: false
    })
  },

  /*vitePlugin: {
		experimental: {
		  inspector: true, // only in dev
		},
	},*/
};